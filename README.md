# PS-MCP

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-1.26.0+-green.svg)](https://github.com/modelcontextprotocol/python-sdk)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

**Photoshop MCP Server - AI驱动的设计工作流自动化**

</div>

---

## 📋 项目简介

**PS-MCP** 是一个基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io) 的 Photoshop 集成服务器，旨在通过 AI 大模型（如 Claude、GPT 等）实现对 Adobe Photoshop 的智能控制。

本项目目前处于**早期开发阶段**，核心目标是实现设计稿的智能切图与资源导出，并计划在未来演进为 **「设计稿分析 → 智能切图 → UI 代码生成」** 的一站式工作流解决方案。

---

## 🎯 项目愿景

### 第一阶段：智能切图（当前重点）
- ✅ 通过自然语言指令控制 Photoshop 导出切片
- ✅ 自动识别设计稿中的图层、组件边界
- ✅ 支持多种格式导出（PNG、JPG、SVG、WebP）
- ✅ 智能命名与资源管理

### 第二阶段：设计稿解析
- 🔄 图层结构分析与语义理解
- 🔄 颜色、字体、间距等设计规范提取
- 🔄 组件库识别与归类

### 第三阶段：UI 代码生成
- 📋 基于切图结果生成前端代码（Vue/React/HTML）
- 📋 自动应用设计规范（Tailwind/UnoCSS）
- 📋 实现「设计稿 → 可运行代码」的完整闭环

---

## 🏗️ 技术架构

```
┌─────────────────────────────────────────────────────────────┐
│                     AI 大模型 (Claude/GPT)                    │
└───────────────────────┬─────────────────────────────────────┘
                        │ MCP Protocol
┌───────────────────────┼─────────────────────────────────────┐
│                       ▼                                     │
│              ┌────────────────┐                            │
│              │   PS-MCP Server │  ← 本项目                 │
│              │   (Python)     │                            │
│              └───────┬────────┘                            │
│                      │                                      │
│          ┌───────────┴───────────┐                         │
│          │                       │                         │
│          ▼                       ▼                         │
│   ┌──────────────┐      ┌──────────────┐                  │
│   │  Photoshop   │      │   Export     │                  │
│   │   JSX/Script │      │   Assets     │                  │
│   └──────────────┘      └──────────────┘                  │
└─────────────────────────────────────────────────────────────┘
```

### 核心技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| MCP Server | [FastMCP](https://github.com/modelcontextprotocol/python-sdk) | Python MCP 服务端框架 |
| 通信协议 | stdio/sse | 标准输入输出 / HTTP 流 |
| PS 交互 | ExtendScript / UXP | Adobe Photoshop 脚本接口 |
| 构建工具 | uv | 现代 Python 包管理器 |

---

## 🚀 快速开始

### 环境要求

- Python >= 3.14
- Adobe Photoshop 2022 或更高版本
- Claude Desktop / 其他 MCP 客户端

### 安装

```bash
# 克隆仓库
git clone https://github.com/pangxie231/ps-mcp.git
cd ps-mcp

# 使用 uv 安装依赖
uv sync

# 或使用 pip
pip install -e "."
```

### 配置 MCP 客户端

在 Claude Desktop 配置文件中添加：

```json
{
  "mcpServers": {
    "ps-mcp": {
      "command": "python",
      "args": ["/path/to/ps-mcp/server.py"]
    }
  }
}
```

### 运行

```bash
# 开发模式
python server.py

# 或使用 uv
uv run server.py
```

---

## 📊 开发进度

| 功能模块 | 状态 | 说明 |
|---------|------|------|
| MCP 服务框架 | ✅ | 基础服务搭建完成 |
| 工具注册 | ✅ | 测试工具可用 |
| PS 连接层 | 🚧 | 开发中... |
| 切图功能 | 📋 | 计划中 |
| 图层分析 | 📋 | 计划中 |
| UI 生成 | 📋 | 计划中 |

**图例：** ✅ 已完成 | 🚧 进行中 | 📋 计划中

---

## 🔧 可用工具

> ⚠️ **注意**：以下工具列表将随开发进度持续更新

### 基础工具

| 工具名 | 描述 | 参数 |
|--------|------|------|
| `hello` | 测试连接 | 无 |

---

## 🤝 参与贡献

本项目欢迎贡献！由于处于早期阶段，API 和架构可能会有较大变动，建议先通过 Issue 讨论后再提交 PR。

### 贡献流程

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add some amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

---

## 📝 开发计划

### 近期目标 (v0.2.0)
- [ ] 实现 Photoshop 基础连接
- [ ] 添加图层信息获取工具
- [ ] 实现简单切片导出功能

### 中期目标 (v0.5.0)
- [ ] 智能组件识别
- [ ] 批量切图导出
- [ ] 设计规范提取

### 远期目标 (v1.0.0)
- [ ] UI 代码生成（支持 Vue/React）
- [ ] 完整的设计到代码工作流
- [ ] 插件生态支持

---

## 📄 许可证

[MIT](LICENSE) © 2026 ps-mcp Contributors

---

<div align="center">

**⚠️ 免责声明**：本项目目前处于早期开发阶段，API 可能不稳定，不建议用于生产环境。

*Made with ❤️ for better design-to-code workflow*

</div>
