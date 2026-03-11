import json
import time
import win32com.client
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PS MCP")

JSX_PATH = "E:/private/ps-mcp/get_layers.jsx"
OUTPUT_PATH = r"E:\private\ps-mcp\ps_output.json"

@mcp.tool()
def get_layer_structure() -> str:
  """读取当前 PS 文档的图层结构"""
  # 连接已打开的 PS，执行脚本
  ps_app = win32com.client.Dispatch("Photoshop.Application")
  ps_app.DoJavaScriptFile(JSX_PATH)

  # 等脚本写完文件
  time.sleep(1)

  # 读取结果
  with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

  return json.dumps(data, ensure_ascii=False, indent=2)

if __name__ == "__main__":
  mcp.run(transport="stdio")