import json
import time
import win32com.client
from mcp.server.fastmcp import FastMCP
import photoshop.api as ps
from photoshop import Session
import os.path
import time
from pathlib import Path



mcp = FastMCP("PS MCP")

# 缓存图层

# 获取文档尺寸
@mcp.tool()
def get_document_info() -> str:
  """获取PSD文档的尺寸信息"""
  
  with Session() as ps:
    doc = ps.app.activeDocument
    return json.dumps({
      "w": doc.width,
      "h": doc.height,
    })


# 内置工具函数
# 获取平坦的所有图层
def find_all_layers(layerSet):
  
  layers = []
  for layer in layerSet.layers:
    if layer.typename == "ArtLayer":
      layers.append(layer)
    elif layer.typename == "LayerSet":
      find_all_layers(layer)

  return layers
    

@mcp.tool()
def export_doc()-> str:
  """
  Args None
  Returns 返回导出图片的路径
  将当前文档导出为一张图片
  导出图片，返回图片路径，然后AI根据视觉能力分析出大概的布局，然后决定要切的图片资源

  当需要AI根据自身经验进行切图时
  当前需要分析html布局信息时、分析前端布局信息时、前端页面结构时
  
  """
  with Session() as ps:
    app = ps.app
    doc = app.activeDocument

    # 储存路径
    # 图片保存参数
    # 是否作为一个副本保存(如果为True，也就是如果保存为.png,但是不会覆盖这个.psd)
    # 扩展名，大写、小写、或者none
    try:
      doc.saveAs("E:/private/ps-mcp/outputs/design.png", ps.PNGSaveOptions())
    except:
      return "出错了"
    
    # filepath = os.path.join(os.getcwd(), "design.png")
    return "E:/private/ps-mcp/outputs/design.png"

# 获取所有的图层信息
@mcp.tool()
def get_all_layers() -> str:
  """
  Args None
  Returns 返回所有的图层信息
  
  Description 
  获取所有的图层，适用于从图层中找出所需要的图层
  """
  app = ps.Application()
  doc = app.activeDocument
  layers = find_all_layers(doc)

  result = []
  for layer in layers:
    info = {
      "name": layer.name,
      "visible": layer.visible,
      "bounds": list(layer.bounds)
    }
    result.append(info)

  return json.dumps({
    "all_layers": result
  })
  
  
# 根据图层名称将图层导出
@mcp.tool()
def export_layer(layer_name, output_dir) -> str:
  """
    Args: 
      layer_name 要导出的图层名称
      output_dir 导出到的文件夹

    Description: 将指定图层导出为图片，通常导出为.png。用于导出图片、切图等场景。
  """
  if os.path.isfile(output_dir):
    return f"{output_dir} 目录有误，传入的目录为一个文件"
  
  if not os.path.exists(output_dir):
    return f"{output_dir} 目录不存在"

  with Session() as ps:

    app = ps.app
    # ps.active_document.trim(ps.TrimType.TransparentPixels)

    # layer = ps.active_document.layers[0]
    # temp_doc = ps.app.documents.add(200, 200)
    # layer.duplicate(temp_doc)
    # temp_doc.close()


    temp_doc = app.activeDocument.duplicate(name="New_Doc")
    app.activeDocument = temp_doc
    
    layers = find_all_layers(temp_doc)

    target_layer = None
    for layer in layers:
      if layer.name == layer_name:
        target_layer = layer
        layer.visible = True
      
      else:
        layer.visible = False
        
    if target_layer:
      file_path = (Path(output_dir) / f"{target_layer.name}.png").as_posix()
      # return file_path
      temp_doc.trim(ps.TrimType.TransparentPixels)
      temp_doc.saveAs(file_path, ps.PNGSaveOptions())
      temp_doc.close()
      return f"已经切出指定图层，图层名称: {layer_name}"
    else:
      return f"未找到相关图层。图层名称:{layer_name}"

        



if __name__ == "__main__":
  mcp.run(transport="stdio")