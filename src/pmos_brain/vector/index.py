#!/usr/bin/env python3
"""
Brain Vector Index -- numpy-based semantic search for Brain entities.

Provides embedding-powered fuzzy search across Brain entities using
sentence-transformers for encoding and a flat numpy matrix for storage.
Exact cosine search; at Brain scale (thousands of entities, 384 dims) a
brute-force matrix product is a few milliseconds, so no ANN index or vector
database is needed. ChromaDB was removed 2026-11-09 (CVE-2026-45829).

Usage:
    python3 index.py build              # Build/rebuild full index
    python3 index.py query "search text" # Query the index
    python3 index.py stats              # Show index statistics
"""

import argparse
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

# Optional dependencies -- graceful degradation if not installed
try:
    import numpy as np

    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

try:
    from sentence_transformers import SentenceTransformer

    HAS_SENTENCE_TRANSFORMERS = True
except ImportError:
    HAS_SENTENCE_TRANSFORMERS = False


VECTOR_AVAILABLE = HAS_NUMPY and HAS_SENTENCE_TRANSFORMERS


class BrainVectorIndex:
    """
    Numpy-backed vector index for semantic search across Brain entities.

    Embeds entity content (name + body text) using sentence-transformers.
    Normalized embeddings live in <brain>/.vector_index/embeddings.npy, with
    ids, documents and metadata in meta.json. Both files are written to a temp
    file and renamed, so readers never see a half-written index.
    """

    DEFAULT_MODEL = "all-MiniLM-L6-v2"
    INDEX_DIR_NAME = ".vector_index"
    EMBEDDINGS_FILE = "embeddings.npy"
    META_FILE = "meta.json"
    # 6.0 = numpy storage. A meta.json with any other version is ignored and
    # the index rebuilds on first query.
    SCHEMA_VERSION = "6.0"

    # Directories to exclude from indexing
    EXCLUDE_DIRS = {"Inbox", "Archive", "__pycache__", ".snapshots", ".schema"}
    EXCLUDE_FILES = {"BRAIN.md", "README.md", "index.md", "_index.md"}

    def __init__(
        self,
        brain_path: Path,
        model_name: str = DEFAULT_MODEL,
    ):
        """
        Initialize the vector index.

        Args:
            brain_path: Path to brain directory
            model_name: sentence-transformers model name (default: all-MiniLM-L6-v2)
        """
        if not VECTOR_AVAILABLE:
            missing = []
            if not HAS_NUMPY:
                missing.append("numpy")
            if not HAS_SENTENCE_TRANSFORMERS:
                missing.append("sentence-transformers")
            raise ImportError(
                f"Missing dependencies: {', '.join(missing)}. "
                f"Install with: pip install {' '.join(missing)}"
            )

        self.brain_path = Path(brain_path)
        self.model_name = model_name
        self._model = None
        self._ids: List[str] = []
        self._documents: List[str] = []
        self._metadatas: List[Dict[str, Any]] = []
        self._embeddings = None
        self._loaded_mtime: Optional[float] = None

        # Index location
        self.index_path = self.brain_path / self.INDEX_DIR_NAME

    @property
    def model(self) -> "SentenceTransformer":
        """Lazy-load the embedding model, preferring local cache to avoid network latency."""
        if self._model is None:
            try:
                self._model = SentenceTransformer(self.model_name, local_files_only=True)
            except Exception:
                # First run or cache miss -- download from HuggingFace
                self._model = SentenceTransformer(self.model_name)
        return self._model

    # -----------------------------------------------------------------------
    # Storage
    # -----------------------------------------------------------------------

    @property
    def _meta_path(self) -> Path:
        return self.index_path / self.META_FILE

    @property
    def _embeddings_path(self) -> Path:
        return self.index_path / self.EMBEDDINGS_FILE

    def _ensure_loaded(self) -> None:
        """Load the index from disk, reloading if another process rewrote it."""
        try:
            mtime = self._meta_path.stat().st_mtime
        except FileNotFoundError:
            self._reset_memory()
            self._loaded_mtime = None
            return
        if mtime == self._loaded_mtime:
            return
        try:
            meta = json.loads(self._meta_path.read_text(encoding="utf-8"))
            if meta.get("schema_version") != self.SCHEMA_VERSION:
                print(
                    f"Vector index schema outdated (upgrading to v{self.SCHEMA_VERSION}), will rebuild",
                    file=sys.stderr,
                )
                self._reset_memory()
            else:
                embeddings = np.load(self._embeddings_path)
                if len(embeddings) != len(meta["ids"]):
                    raise ValueError("embeddings and meta.json row counts differ")
                self._ids = list(meta["ids"])
                self._documents = list(meta["documents"])
                self._metadatas = list(meta["metadatas"])
                self._embeddings = embeddings
        except Exception as e:
            print(f"Vector index unreadable ({e}), will rebuild", file=sys.stderr)
            self._reset_memory()
        self._loaded_mtime = mtime

    def _reset_memory(self) -> None:
        self._ids, self._documents, self._metadatas = [], [], []
        self._embeddings = None

    def _save(self) -> None:
        """Write embeddings then meta.json atomically. meta.json is the commit marker."""
        self.index_path.mkdir(parents=True, exist_ok=True)
        embeddings = (
            self._embeddings
            if self._embeddings is not None
            else np.zeros((0, 0), dtype=np.float32)
        )
        fd, tmp = tempfile.mkstemp(dir=self.index_path, suffix=".npy.tmp")
        with os.fdopen(fd, "wb") as f:
            np.save(f, embeddings)
        os.replace(tmp, self._embeddings_path)

        meta = {
            "schema_version": self.SCHEMA_VERSION,
            "model": self.model_name,
            "ids": self._ids,
            "documents": self._documents,
            "metadatas": self._metadatas,
        }
        fd, tmp = tempfile.mkstemp(dir=self.index_path, suffix=".json.tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(meta, f)
        os.replace(tmp, self._meta_path)
        self._loaded_mtime = self._meta_path.stat().st_mtime

    def _remove_legacy_chroma(self) -> None:
        """Delete files left by the pre-6.0 ChromaDB index (chroma.sqlite3 + segment dirs)."""
        if not self.index_path.exists():
            return
        legacy = self.index_path / "chroma.sqlite3"
        if legacy.exists():
            legacy.unlink()
        for child in self.index_path.iterdir():
            if child.is_dir() and (child / "header.bin").exists():
                shutil.rmtree(child, ignore_errors=True)

    def count(self) -> int:
        """Number of entities in the index."""
        self._ensure_loaded()
        return len(self._ids)

    def _encode(self, texts: List[str]) -> "np.ndarray":
        return np.asarray(
            self.model.encode(texts, normalize_embeddings=True), dtype=np.float32
        )

    def build_index(self) -> Dict[str, Any]:
        """
        Build the full vector index from all Brain entities.

        Scans all markdown files in the brain directory, extracts
        frontmatter metadata and body text, generates embeddings,
        and writes them to disk.

        Returns:
            Dict with build statistics: entities_indexed, errors, duration
        """
        entities = self._scan_entities()

        if not entities:
            return {"entities_indexed": 0, "errors": 0, "message": "No entities found"}

        # Prepare data for batch insert
        ids = []
        documents = []
        metadatas = []

        for entity_id, entity_data in entities.items():
            doc_text = self._build_document_text(entity_data)
            if not doc_text.strip():
                continue

            ids.append(entity_id)
            documents.append(doc_text)
            metadatas.append(self._sanitize_metadata(entity_id, entity_data))

        # Batch embed; a failed batch is skipped, not fatal
        errors = 0
        batch_size = 100
        kept_ids: List[str] = []
        kept_docs: List[str] = []
        kept_meta: List[Dict[str, Any]] = []
        chunks = []
        for i in range(0, len(ids), batch_size):
            batch_docs = documents[i : i + batch_size]
            try:
                chunks.append(self._encode(batch_docs))
            except Exception as e:
                errors += 1
                print(f"Error indexing batch {i // batch_size}: {e}", file=sys.stderr)
                continue
            kept_ids.extend(ids[i : i + batch_size])
            kept_docs.extend(batch_docs)
            kept_meta.extend(metadatas[i : i + batch_size])

        self._ids, self._documents, self._metadatas = kept_ids, kept_docs, kept_meta
        self._embeddings = np.vstack(chunks) if chunks else None
        self._save()
        self._remove_legacy_chroma()

        return {
            "entities_indexed": len(self._ids),
            "total_scanned": len(entities),
            "errors": errors,
        }

    def query(
        self,
        text: str,
        top_k: int = 10,
        entity_type: Optional[str] = None,
        min_confidence: Optional[float] = None,
    ) -> List[Dict[str, Any]]:
        """
        Query the vector index for semantically similar entities.

        Args:
            text: Natural language query text
            top_k: Number of results to return
            entity_type: Filter by entity $type (e.g., "project", "person")
            min_confidence: Filter by minimum $confidence score

        Returns:
            List of result dicts with keys:
                entity_id, entity_path, score, snippet, metadata
        """
        if self.count() == 0:
            # Auto-rebuild if index is empty
            print("Vector index empty, rebuilding...", file=sys.stderr)
            self.build_index()
            if self.count() == 0:
                return []

        # Rows eligible for this query (type filter applies before top-k)
        if entity_type:
            candidates = np.array(
                [
                    i
                    for i, m in enumerate(self._metadatas)
                    if m.get("entity_type") == entity_type
                ],
                dtype=np.int64,
            )
        else:
            candidates = np.arange(len(self._ids))
        if candidates.size == 0:
            return []

        # Embeddings are normalized, so the dot product is cosine similarity
        query_embedding = self._encode([text])[0]
        sims = self._embeddings[candidates] @ query_embedding
        k = min(top_k, candidates.size)
        top = np.argpartition(-sims, k - 1)[:k]
        top = top[np.argsort(-sims[top], kind="stable")]

        output = []
        for t in top:
            row = int(candidates[t])
            metadata = self._metadatas[row]
            document = self._documents[row]

            # Apply post-query confidence filter
            if min_confidence is not None:
                if metadata.get("confidence", 0.0) < min_confidence:
                    continue

            # Same scale as the pre-6.0 ChromaDB index: cosine distance d = 1 - cos,
            # score = 1 - d/2, so 1 = identical and 0 = opposite.
            score = 1.0 - (1.0 - float(sims[t])) / 2.0

            output.append(
                {
                    "entity_id": self._ids[row],
                    "entity_path": metadata.get("file_path", ""),
                    "score": round(score, 4),
                    "snippet": document[:200] if document else "",
                    "metadata": metadata,
                }
            )

        return output

    def add_entity(self, entity_path: Path) -> bool:
        """
        Add or update a single entity in the index.

        Args:
            entity_path: Path to the entity markdown file

        Returns:
            True if successfully added/updated
        """
        try:
            entity_data = self._parse_entity_file(entity_path)
            if not entity_data:
                return False

            entity_id = entity_data.get(
                "$id", str(entity_path.relative_to(self.brain_path))
            )
            doc_text = self._build_document_text(entity_data)

            if not doc_text.strip():
                return False

            embedding = self._encode([doc_text])

            metadata = self._sanitize_metadata(entity_id, entity_data)
            metadata["file_path"] = str(entity_path)

            self._ensure_loaded()
            if entity_id in self._ids:
                row = self._ids.index(entity_id)
                self._documents[row] = doc_text
                self._metadatas[row] = metadata
                self._embeddings[row] = embedding[0]
            else:
                self._ids.append(entity_id)
                self._documents.append(doc_text)
                self._metadatas.append(metadata)
                self._embeddings = (
                    embedding
                    if self._embeddings is None
                    else np.vstack([self._embeddings, embedding])
                )
            self._save()
            return True

        except Exception as e:
            print(f"Error adding entity {entity_path}: {e}", file=sys.stderr)
            return False

    def remove_entity(self, entity_id: str) -> bool:
        """
        Remove an entity from the index.

        Args:
            entity_id: The entity's $id to remove

        Returns:
            True if successfully removed
        """
        try:
            self._ensure_loaded()
            if entity_id in self._ids:
                row = self._ids.index(entity_id)
                del self._ids[row], self._documents[row], self._metadatas[row]
                self._embeddings = np.delete(self._embeddings, row, axis=0)
                self._save()
            return True
        except Exception as e:
            print(f"Error removing entity {entity_id}: {e}", file=sys.stderr)
            return False

    def rebuild(self) -> Dict[str, Any]:
        """
        Full rebuild of the vector index. Alias for build_index().

        Returns:
            Build statistics dict
        """
        return self.build_index()

    def get_stats(self) -> Dict[str, Any]:
        """
        Get index statistics.

        Returns:
            Dict with entity_count and index_path
        """
        return {
            "entity_count": self.count(),
            "index_path": str(self.index_path),
        }

    # -----------------------------------------------------------------------
    # Internal helpers
    # -----------------------------------------------------------------------

    def _sanitize_metadata(
        self, entity_id: str, entity_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Flatten entity metadata to JSON scalars (str, float); no $ in keys."""
        raw_conf = entity_data.get("$confidence")
        try:
            confidence = float(raw_conf) if raw_conf is not None else 0.0
        except (ValueError, TypeError):
            confidence = 0.0

        raw_name = entity_data.get("name", entity_data.get("$id", entity_id))
        name = str(raw_name) if raw_name is not None else entity_id

        return {
            "entity_type": str(entity_data.get("$type", "unknown") or "unknown"),
            "entity_status": str(entity_data.get("$status", "unknown") or "unknown"),
            "confidence": confidence,
            "file_path": str(entity_data.get("_path", "")),
            "name": name,
        }

    def _scan_entities(self) -> Dict[str, Dict[str, Any]]:
        """Scan all Brain entity files and parse their metadata."""
        entities = {}

        for md_file in self.brain_path.rglob("*.md"):
            # Skip excluded directories
            if any(excluded in md_file.parts for excluded in self.EXCLUDE_DIRS):
                continue
            # Skip excluded files
            if md_file.name in self.EXCLUDE_FILES:
                continue

            try:
                entity_data = self._parse_entity_file(md_file)
                if not entity_data:
                    continue

                entity_id = entity_data.get(
                    "$id", str(md_file.relative_to(self.brain_path))
                )
                entity_data["_path"] = md_file
                entities[entity_id] = entity_data

            except Exception:
                continue

        return entities

    def _parse_entity_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Parse a markdown file's YAML frontmatter and body."""
        try:
            content = file_path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, IOError):
            return None

        if not content.startswith("---"):
            return None

        parts = content.split("---", 2)
        if len(parts) < 3:
            return None

        try:
            frontmatter = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            return None

        frontmatter["_body"] = parts[2].strip()
        frontmatter["_name"] = file_path.stem.replace("_", " ")
        return frontmatter

    def _build_document_text(self, entity_data: Dict[str, Any]) -> str:
        """Build the document text for embedding from entity data."""
        parts = []

        # Entity name (high weight via repetition)
        name = entity_data.get("name", entity_data.get("_name", ""))
        if name:
            parts.append(name)

        # Description
        desc = entity_data.get("description", "")
        if desc:
            parts.append(str(desc))

        # Body content (first 500 chars for efficiency)
        body = entity_data.get("_body", "")
        if body:
            parts.append(body[:500].strip())

        # Tags
        tags = entity_data.get("$tags", [])
        if tags and isinstance(tags, list):
            parts.append(" ".join(str(t) for t in tags))

        return " ".join(parts)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Brain Vector Index (numpy)"
    )
    parser.add_argument(
        "action",
        choices=["build", "query", "stats", "rebuild"],
        help="Action to perform",
    )
    parser.add_argument(
        "query_text",
        nargs="?",
        help="Query text (for query action)",
    )
    parser.add_argument(
        "--brain-path",
        type=Path,
        help="Path to brain directory",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=BrainVectorIndex.DEFAULT_MODEL,
        help=f"Embedding model (default: {BrainVectorIndex.DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=10,
        help="Number of results (default: 10)",
    )
    parser.add_argument(
        "--type",
        type=str,
        help="Filter by entity type",
    )
    parser.add_argument(
        "--output",
        choices=["text", "json"],
        default="text",
        help="Output format",
    )

    args = parser.parse_args()

    if not VECTOR_AVAILABLE:
        missing = []
        if not HAS_NUMPY:
            missing.append("numpy")
        if not HAS_SENTENCE_TRANSFORMERS:
            missing.append("sentence-transformers")
        print(
            f"Error: Missing dependencies: {', '.join(missing)}\n"
            f"Install with: pip install {' '.join(missing)}",
            file=sys.stderr,
        )
        return 1

    # Resolve brain path
    brain_path = Path(args.brain_path) if args.brain_path else Path.cwd()

    index = BrainVectorIndex(brain_path, model_name=args.model)

    if args.action in ("build", "rebuild"):
        print(f"Building vector index from {brain_path}...")
        stats = index.build_index()

        if args.output == "json":
            print(json.dumps(stats, indent=2))
        else:
            print(f"Entities indexed: {stats['entities_indexed']}")
            print(f"Total scanned: {stats.get('total_scanned', 0)}")
            print(f"Errors: {stats['errors']}")
            print(f"Index location: {index.index_path}")

    elif args.action == "query":
        if not args.query_text:
            print("Error: query action requires query text", file=sys.stderr)
            return 1

        results = index.query(
            args.query_text,
            top_k=args.top_k,
            entity_type=args.type,
        )

        if args.output == "json":
            print(json.dumps(results, indent=2))
        else:
            print(f"Query: {args.query_text}")
            print(f"Results ({len(results)}):")
            print("-" * 60)
            for r in results:
                print(f"  {r['score']:.3f} | {r['entity_id']}")
                print(f"         {r['metadata'].get('entity_type', '?')} | {r['entity_path']}")
                if r.get("snippet"):
                    print(f"         {r['snippet'][:80]}...")
                print()

    elif args.action == "stats":
        stats = index.get_stats()
        if args.output == "json":
            print(json.dumps(stats))
        else:
            print(f"Index location: {stats['index_path']}")
            print(f"Entities in index: {stats['entity_count']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
