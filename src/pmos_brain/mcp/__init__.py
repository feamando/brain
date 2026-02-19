"""Brain MCP Server for AI agent integration."""
try:
    from pmos_brain.mcp.server import mcp
    MCP_AVAILABLE = True
except ImportError:
    mcp = None
    MCP_AVAILABLE = False

__all__ = ["mcp", "MCP_AVAILABLE"]
