import json
import time
import win32com.client
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PS MCP")




if __name__ == "__main__":
  mcp.run(transport="stdio")