import json
import time
import win32com.client
from mcp.server.fastmcp import FastMCP
import photoshop.api as ps
from photoshop import Session
import json

mcp = FastMCP("PS MCP")

# 打开 psd 文档
@mcp.tool()
def open_psd(file_path) -> str:
  """接收一个文件路径，然后用photoshop打开它"""
  with Session(file_path, action="open") as ps:
    doc = ps.active_document
  return "打开成功"


# 获取文档尺寸和图层树
@mcp.tool()
def get_document_info() -> str:
  """获取PSD文件的基本信息，包括文档尺寸和图层树信息"""
  app = ps.Application()
  doc = app.activeDocument

  return json.dumps({
    "w": doc.width,
    "h": doc.height,
  })
  


if __name__ == "__main__":
  mcp.run(transport="stdio")