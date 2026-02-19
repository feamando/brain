#!/usr/bin/env python3
"""
Brain Search - Keyword and Semantic Search Component

Implements keyword search across aliases and content using:
- O(1) alias lookup via registry alias_index
- O(1) content lookup via inverted index
- Query expansion for common synonyms
- AND semantics for multi-word queries
- Relevance scoring
- Optional semantic (vector) search fallback
"""

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# Try to import yaml
try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# Scoring weights
SCORE_ALIAS_EXACT = 1.0
SCORE_ALIAS_PARTIAL = 0.5
SCORE_CONTENT_TITLE = 0.3
SCORE_CONTENT_BODY = 0.1


# ---------------------------------------------------------------------------
# Minimal Porter Stemmer (suffix-stripping rules, no external dependencies)
# ---------------------------------------------------------------------------

class PorterStemmer:
    """Simplified Porter stemmer for English word normalization."""

    def __init__(self):
        self.cache: Dict[str, str] = {}

    def stem(self, word: str) -> str:
        """Stem a word to its root form."""
        if word in self.cache:
            return self.cache[word]

        word = word.lower()
        if len(word) <= 2:
            return word

        original = word

        # Step 1a: plurals
        if word.endswith("sses"):
            word = word[:-2]
        elif word.endswith("ies"):
            word = word[:-2]
        elif word.endswith("ss"):
            pass
        elif word.endswith("s"):
            word = word[:-1]

        # Step 1b: -eed, -ed, -ing
        if word.endswith("eed"):
            if len(word) > 4:
                word = word[:-1]
        elif word.endswith("ed"):
            if self._has_vowel(word[:-2]):
                word = word[:-2]
                word = self._step1b_fixup(word)
        elif word.endswith("ing"):
            if self._has_vowel(word[:-3]):
                word = word[:-3]
                word = self._step1b_fixup(word)

        # Step 2: common suffix replacements
        replacements = [
            ("ational", "ate"),
            ("tional", "tion"),
            ("enci", "ence"),
            ("anci", "ance"),
            ("izer", "ize"),
            ("ation", "ate"),
            ("ator", "ate"),
            ("alism", "al"),
            ("iveness", "ive"),
            ("fulness", "ful"),
            ("ousness", "ous"),
            ("aliti", "al"),
            ("iviti", "ive"),
            ("biliti", "ble"),
        ]
        for suffix, replacement in replacements:
            if word.endswith(suffix) and len(word) > len(suffix) + 2:
                word = word[: -len(suffix)] + replacement
                break

        # Step 3-5: additional simplification
        if word.endswith("icate") and len(word) > 7:
            word = word[:-3]
        elif word.endswith("ative") and len(word) > 7:
            word = word[:-5]
        elif word.endswith("alize") and len(word) > 7:
            word = word[:-3]
        elif word.endswith("ful") and len(word) > 5:
            word = word[:-3]
        elif word.endswith("ness") and len(word) > 6:
            word = word[:-4]

        self.cache[original] = word
        return word

    def _has_vowel(self, word: str) -> bool:
        """Check if word contains a vowel."""
        return bool(re.search(r"[aeiou]", word))

    def _step1b_fixup(self, word: str) -> str:
        """Fix up word after step 1b."""
        if word.endswith(("at", "bl", "iz")):
            return word + "e"
        if len(word) > 2 and word[-1] == word[-2] and word[-1] not in "lsz":
            return word[:-1]
        return word


# ---------------------------------------------------------------------------
# Search result dataclass
# ---------------------------------------------------------------------------

@dataclass
class SearchResult:
    """Single search result with relevance info."""

    entity_id: str
    score: float
    source: str  # 'alias', 'content', 'semantic'
    match_reasons: List[str] = field(default_factory=list)
    file_path: Optional[str] = None
    via: Optional[str] = None  # For graph results: which entity led here
    relationship_type: Optional[str] = None

    def __hash__(self):
        return hash(self.entity_id)

    def __eq__(self, other):
        return isinstance(other, SearchResult) and self.entity_id == other.entity_id


# ---------------------------------------------------------------------------
# BrainSearch
# ---------------------------------------------------------------------------

class BrainSearch:
    """
    Brain keyword search component.

    Combines alias matching (fast, exact) with content search (via inverted index).
    Implements query expansion and relevance scoring.
    """

    def __init__(
        self,
        brain_path: Optional[Path] = None,
        registry: Optional[Dict] = None,
    ):
        self.brain_path = Path(brain_path) if brain_path else Path.cwd()
        self.registry_file = self.brain_path / "registry.yaml"
        self.index_file = self.brain_path / "content_index.json"
        self.stemmer = PorterStemmer()

        # Load registry and build alias index
        self.registry = registry if registry else self._load_registry()
        self.alias_index = self._build_alias_index()

        # Load content index
        self.content_index = self._load_content_index()

        # Query expansion dictionary (synonyms)
        self.synonyms = self._build_synonym_dict()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def search(
        self,
        query: str,
        entity_type: Optional[str] = None,
        limit: int = 20,
    ) -> List[SearchResult]:
        """
        Search for entities matching query.

        Args:
            query: Natural language search query
            entity_type: Optional entity type filter (currently unused by
                keyword search but kept for interface compatibility)
            limit: Maximum results to return

        Returns:
            List of SearchResult sorted by relevance score
        """
        if not query or not query.strip():
            return []

        query = query.strip()

        # 1. Alias matches (O(1) per alias)
        alias_results = self._search_aliases(query)

        # 2. Content matches via inverted index
        content_results = self._search_content(query)

        # 3. Merge and rank (dedup, max score wins)
        merged = self._merge_results(alias_results, content_results)

        # 4. Sort by score and return top results
        merged.sort(key=lambda r: -r.score)

        return merged[:limit]

    def semantic_search(
        self,
        query: str,
        limit: int = 10,
        entity_type: Optional[str] = None,
    ) -> List[SearchResult]:
        """
        Semantic search using vector embeddings via BrainVectorIndex.

        Falls back gracefully if chromadb/sentence-transformers not installed.

        Args:
            query: Natural language search query
            limit: Maximum results to return
            entity_type: Filter by entity type

        Returns:
            List of SearchResult sorted by similarity score
        """
        try:
            from pmos_brain.vector.index import BrainVectorIndex, VECTOR_AVAILABLE
        except ImportError:
            return []

        if not VECTOR_AVAILABLE:
            return []

        try:
            index = BrainVectorIndex(self.brain_path)
            results = index.query(query, top_k=limit, entity_type=entity_type)

            return [
                SearchResult(
                    entity_id=r["entity_id"],
                    score=r["score"],
                    source="semantic",
                    match_reasons=[f"vector similarity: {r['score']:.3f}"],
                    file_path=r.get("entity_path", ""),
                )
                for r in results
            ]
        except Exception as e:
            print(f"Semantic search error: {e}", file=sys.stderr)
            return []

    # ------------------------------------------------------------------
    # Alias search
    # ------------------------------------------------------------------

    def _search_aliases(self, query: str) -> List[SearchResult]:
        """Search aliases for exact and partial matches."""
        results: Dict[str, SearchResult] = {}
        query_lower = query.lower()
        query_terms = query_lower.split()

        # Exact match on full query
        if query_lower in self.alias_index:
            cat, entity_id, file_path = self.alias_index[query_lower]
            results[entity_id] = SearchResult(
                entity_id=entity_id,
                score=SCORE_ALIAS_EXACT,
                source="alias",
                match_reasons=[f'alias exact: "{query_lower}"'],
                file_path=file_path,
            )

        # Partial matches (each query term)
        for term in query_terms:
            if len(term) < 2:
                continue

            # Exact match on term
            if term in self.alias_index:
                cat, entity_id, file_path = self.alias_index[term]
                if entity_id not in results:
                    results[entity_id] = SearchResult(
                        entity_id=entity_id,
                        score=SCORE_ALIAS_PARTIAL,
                        source="alias",
                        match_reasons=[f'alias term: "{term}"'],
                        file_path=file_path,
                    )
                else:
                    results[entity_id].match_reasons.append(f'alias term: "{term}"')
                    # Boost score for multiple term matches
                    results[entity_id].score = min(
                        1.0, results[entity_id].score + 0.1
                    )

            # Prefix matching on aliases (for partial word matches)
            for alias, (cat, entity_id, file_path) in self.alias_index.items():
                if alias.startswith(term) and len(alias) <= len(term) + 3:
                    if entity_id not in results:
                        results[entity_id] = SearchResult(
                            entity_id=entity_id,
                            score=SCORE_ALIAS_PARTIAL * 0.8,  # slightly lower for prefix
                            source="alias",
                            match_reasons=[f'alias prefix: "{term}" -> "{alias}"'],
                            file_path=file_path,
                        )

        return list(results.values())

    # ------------------------------------------------------------------
    # Content search (inverted index)
    # ------------------------------------------------------------------

    def _search_content(self, query: str) -> List[SearchResult]:
        """Search content via inverted index with AND semantics."""
        if not self.content_index:
            return []

        # Tokenize and stem query
        tokens = self._tokenize_query(query)
        if not tokens:
            return []

        # Expand query with synonyms
        expanded_tokens = self._expand_query(tokens)

        # Get posting lists for each token
        posting_lists: List[Set[str]] = []
        matched_tokens: List[str] = []

        for token in expanded_tokens:
            if token in self.content_index:
                posting_lists.append(set(self.content_index[token]))
                matched_tokens.append(token)

        if not posting_lists:
            return []

        # AND semantics: intersection of all posting lists
        result_set = posting_lists[0]
        for pl in posting_lists[1:]:
            result_set = result_set.intersection(pl)

        # Score based on token coverage
        results: List[SearchResult] = []
        for entity_id in result_set:
            coverage = len(matched_tokens) / len(tokens) if tokens else 0
            score = SCORE_CONTENT_BODY * coverage

            # Boost if entity name contains query terms
            entity_name = entity_id.split("/")[-1].replace("-", " ")
            if any(term in entity_name for term in query.lower().split()):
                score = max(score, SCORE_CONTENT_TITLE)

            results.append(
                SearchResult(
                    entity_id=entity_id,
                    score=score,
                    source="content",
                    match_reasons=[f'content: {", ".join(matched_tokens)}'],
                )
            )

        return results

    # ------------------------------------------------------------------
    # Query processing helpers
    # ------------------------------------------------------------------

    def _tokenize_query(self, query: str) -> List[str]:
        """Tokenize and stem query terms."""
        words = re.findall(r"\b[a-zA-Z][a-zA-Z0-9]*\b", query.lower())

        stopwords = {
            "a", "an", "the", "and", "or", "in", "on", "at", "to", "for",
            "of", "with", "by", "is", "was", "are", "be", "been", "have",
            "has", "had", "do", "does", "did", "will", "would", "could",
            "should", "may", "might", "this", "that", "it", "they", "we",
            "you", "he", "she", "i", "my", "me", "what", "how", "when",
        }

        tokens: List[str] = []
        for word in words:
            if word in stopwords or len(word) < 2:
                continue
            stemmed = self.stemmer.stem(word)
            if len(stemmed) >= 2:
                tokens.append(stemmed)

        return tokens

    def _expand_query(self, tokens: List[str]) -> Set[str]:
        """Expand query tokens with synonyms."""
        expanded = set(tokens)

        for token in tokens:
            if token in self.synonyms:
                expanded.update(self.synonyms[token])

        return expanded

    def _build_synonym_dict(self) -> Dict[str, List[str]]:
        """Build synonym dictionary for query expansion."""
        # Generic technical synonyms only -- no project-specific entries
        raw_synonyms = {
            "launch": ["releas", "deploy", "ship", "rollout"],
            "bug": ["issu", "defect", "error", "problem"],
            "feature": ["function", "capabil"],
            "user": ["custom", "client"],
            "team": ["squad", "group"],
            "test": ["verifi", "valid", "check"],
            "config": ["set", "configur"],
            "auth": ["authent", "login", "signin"],
            "api": ["endpoint", "servic"],
            "db": ["databas", "store"],
            "ui": ["interfac", "frontend", "ux"],
        }

        # Stem all synonyms for consistency
        synonyms: Dict[str, List[str]] = {}
        for key, values in raw_synonyms.items():
            stemmed_key = self.stemmer.stem(key)
            stemmed_values = [self.stemmer.stem(v) for v in values]
            synonyms[stemmed_key] = stemmed_values

            # Bidirectional: each synonym also maps to others
            for v in stemmed_values:
                if v not in synonyms:
                    synonyms[v] = []
                if stemmed_key not in synonyms[v]:
                    synonyms[v].append(stemmed_key)

        return synonyms

    # ------------------------------------------------------------------
    # Merge / dedup
    # ------------------------------------------------------------------

    def _merge_results(
        self,
        alias_results: List[SearchResult],
        content_results: List[SearchResult],
    ) -> List[SearchResult]:
        """Merge results from alias and content search, max score wins on collision."""
        merged: Dict[str, SearchResult] = {}

        # Add alias results first (typically higher scores)
        for r in alias_results:
            merged[r.entity_id] = r

        # Merge content results
        for r in content_results:
            if r.entity_id not in merged:
                merged[r.entity_id] = r
            else:
                existing = merged[r.entity_id]
                if r.score > existing.score:
                    existing.score = r.score
                existing.match_reasons.extend(r.match_reasons)

        return list(merged.values())

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def _load_registry(self) -> Dict:
        """Load registry from YAML file."""
        if not self.registry_file.exists():
            return {}

        try:
            with open(self.registry_file, "r", encoding="utf-8") as f:
                if HAS_YAML:
                    registry = yaml.safe_load(f)
                    # Normalize v2 if needed
                    if registry and "$schema" in registry:
                        return self._normalize_v2_registry(registry)
                    return registry or {}
                else:
                    return {}
        except Exception as e:
            print(f"Error loading registry: {e}", file=sys.stderr)
            return {}

    def _normalize_v2_registry(self, v2_registry: Dict) -> Dict:
        """Normalize v2 registry to v1-compatible structure."""
        v1: Dict[str, Any] = {
            "projects": {},
            "entities": {},
            "architecture": {},
            "decisions": {},
            "_v2_alias_index": v2_registry.get("alias_index", {}),
        }

        entities = v2_registry.get("entities", {})
        for slug, data in entities.items():
            if not isinstance(data, dict):
                continue

            entity_type = data.get("$type", "entity")
            ref = data.get("$ref", "")

            type_to_category = {
                "project": "projects",
                "person": "entities",
                "team": "entities",
                "squad": "entities",
                "system": "entities",
                "brand": "entities",
                "architecture": "architecture",
                "decision": "decisions",
            }
            category = type_to_category.get(entity_type, "entities")

            v1[category][slug] = {"file": ref, "aliases": data.get("aliases", [])}

        return v1

    def _build_alias_index(self) -> Dict[str, Tuple[str, str, str]]:
        """Build reverse alias index from registry for O(1) lookup."""
        index: Dict[str, Tuple[str, str, str]] = {}

        # Use v2 alias index if available
        if "_v2_alias_index" in self.registry and self.registry["_v2_alias_index"]:
            v2_index = self.registry["_v2_alias_index"]
            for alias, slug in v2_index.items():
                for category in ["projects", "entities", "architecture", "decisions"]:
                    if category in self.registry and slug in self.registry[category]:
                        data = self.registry[category][slug]
                        file_path = data.get("file", "")
                        index[alias.lower()] = (category, slug, file_path)
                        break

        # Standard index building
        for category in ["projects", "entities", "architecture", "decisions"]:
            if category not in self.registry or not self.registry[category]:
                continue

            for entity_id, data in self.registry[category].items():
                if not isinstance(data, dict):
                    continue

                file_path = data.get("file", "")
                aliases = data.get("aliases", [])

                for alias in [entity_id] + (aliases if aliases else []):
                    if alias:
                        index[alias.lower()] = (category, entity_id, file_path)

        return index

    def _load_content_index(self) -> Dict[str, List[str]]:
        """Load inverted content index from JSON file."""
        if not self.index_file.exists():
            return {}

        try:
            with open(self.index_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data.get("index", {})
        except Exception as e:
            print(f"Error loading content index: {e}", file=sys.stderr)
            return {}


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    """Search CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Brain Search")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument(
        "--semantic",
        type=str,
        metavar="QUERY",
        help="Semantic search query (vector embeddings)",
    )
    parser.add_argument("--brain-path", type=str, default=".", help="Path to brain directory")
    parser.add_argument("--limit", type=int, default=10, help="Max results")
    parser.add_argument("--type", type=str, help="Filter by entity type (semantic mode only)")
    parser.add_argument(
        "--output",
        choices=["text", "json"],
        default="text",
        help="Output format",
    )

    args = parser.parse_args()

    query_text = args.semantic or args.query

    if not query_text:
        print("Usage: python -m pmos_brain.core.search <query>")
        print("       python -m pmos_brain.core.search --semantic 'query text'")
        return

    brain_path = Path(args.brain_path).resolve()
    search = BrainSearch(brain_path=brain_path)

    if args.semantic:
        results = search.semantic_search(
            query_text, limit=args.limit, entity_type=args.type
        )
        mode = "semantic"
    else:
        results = search.search(query_text, limit=args.limit)
        mode = "keyword"

    if args.output == "json":
        import json as json_mod

        output = [
            {
                "entity_id": r.entity_id,
                "score": r.score,
                "source": r.source,
                "match_reasons": r.match_reasons,
                "file_path": r.file_path,
            }
            for r in results
        ]
        print(json_mod.dumps(output, indent=2))
    else:
        print(f"Query ({mode}): {query_text}")
        print(f"Results ({len(results)}):")
        print("-" * 50)

        for r in results:
            print(f"{r.score:.2f} | {r.entity_id}")
            print(f"      {r.source}: {', '.join(r.match_reasons[:3])}")
            if r.file_path:
                print(f"      path: {r.file_path}")


if __name__ == "__main__":
    main()
