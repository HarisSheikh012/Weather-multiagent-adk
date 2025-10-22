import os
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

# ✅ Define folder for file operations (safe sandbox)
MCP_FILES_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../mcp_files")
)

# Ensure the directory exists
os.makedirs(MCP_FILES_PATH, exist_ok=True)

# ✅ MCP Toolset for File System
filesystem_mcp_toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                MCP_FILES_PATH,  # exposed path
            ],
            startup_timeout=15,  # avoid timeouts on slower systems
        ),
    ),
)

__all__ = ["filesystem_mcp_toolset", "MCP_FILES_PATH"]
