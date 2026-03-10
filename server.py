from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PS MCP")

@mcp.tool()
def hello() -> str:
  """测试工具，返回 Hello World"""
  return "Hello! PS MCP 连接成功 🎉"

if  __name__ == "__main__":
  mcp.run(transport="stdio")