var doc = app.activeDocument;
var result = {
  docName: doc.name,
  width: doc.width.as("px"),
  height: doc.height.as("px"),
  layers: []
};

// 手动实现 JSON.stringify（ExtendScript 不内置）
function toJSON(obj) {
  if (obj === null) return "null";
  if (typeof obj === "boolean") return obj ? "true" : "false";
  if (typeof obj === "number") return String(obj);
  if (typeof obj === "string") return '"' + obj.replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"';
  if (obj instanceof Array) {
    var items = [];
    for (var i = 0; i < obj.length; i++) items.push(toJSON(obj[i]));
    return "[" + items.join(",") + "]";
  }
  if (typeof obj === "object") {
    var pairs = [];
    for (var k in obj) pairs.push('"' + k + '":' + toJSON(obj[k]));
    return "{" + pairs.join(",") + "}";
  }
  return "null";
}

function collectLayers(layers, depth) {
  for (var i = 0; i < layers.length; i++) {
    var layer = layers[i];
    var item = {
      name: layer.name,
      type: layer.typename,
      visible: layer.visible,
      depth: depth,
      bounds: {
        x: Math.round(layer.bounds[0].as("px")),
        y: Math.round(layer.bounds[1].as("px")),
        w: Math.round(layer.bounds[2].as("px") - layer.bounds[0].as("px")),
        h: Math.round(layer.bounds[3].as("px") - layer.bounds[1].as("px"))
      }
    };
    result.layers.push(item);

    if (layer.typename === "LayerSet") {
      collectLayers(layer.layers, depth + 1);
    }
  }
}

collectLayers(doc.layers, 0);

var file = new File("E:/private/ps-mcp/ps_output.json");
file.encoding = "UTF-8";
file.open("w");
file.write(toJSON(result));
file.close();