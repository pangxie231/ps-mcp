from mcp.server.fastmcp import FastMCP
import json
import subprocess

mcp = FastMCP("PS MCP")

PS_PATH = r"C:\Program Files\Adobe\Adobe Photoshop 2023\Photoshop.exe"
JSX_PATH = r"E:\private\ps-mcp\get_layers.jsx"
OUTPUT_PATH = r"E:\private\ps-mcp\ps_output.json"

@mcp.tool()
def hello() -> str:
    """读取当前 PS 文档的图层结构"""
    # 让 PS 执行脚本
    subprocess.run([
        "powershell", "-command",
        f'& "{PS_PATH}" "{JSX_PATH}"'
    ], capture_output=True)

    # 等 PS 执行完，读取结果
    import time
    time.sleep(3)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    return json.dumps(data, ensure_ascii=False, indent=2)

if  __name__ == "__main__":
  mcp.run(transport="stdio")