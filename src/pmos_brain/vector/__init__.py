"""Vector search and embedding-based operations."""
try:
    from pmos_brain.vector.index import BrainVectorIndex
    VECTOR_AVAILABLE = True
except ImportError:
    BrainVectorIndex = None
    VECTOR_AVAILABLE = False

try:
    from pmos_brain.vector.edge_inferrer import EmbeddingEdgeInferrer
except ImportError:
    EmbeddingEdgeInferrer = None
