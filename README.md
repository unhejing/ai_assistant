# 即梦 · AI 生成工作台

基于开源图像生成框架的可扩展AI助手平台，采用Vue3 + Element Plus前端和FastAPI后端架构。

## 🎯 功能特性

### 🎨 图像生成
- **文生图**：输入提示词生成高质量图像
- **图生图**：上传图像结合提示词改造风格
- 支持多种尺寸和参数调节

### 🚀 可扩展模块（预留接口）
- **数字人生成**：会说话的AI数字人视频
- **声音克隆**：个性化语音合成
- **智能体**：基于LLM的对话助手

## 🏗️ 技术架构

### 前端技术栈
- **Vue 3** + **TypeScript** + **Composition API**
- **Element Plus** 组件库
- **Pinia** 状态管理
- **Vue Router** 路由
- **Vite** 构建工具

### 后端技术栈
- **FastAPI** 异步Web框架
- **Pydantic** 数据验证
- **Uvicorn** ASGI服务器
- **Loguru** 日志管理

### 部署方案
- **Docker** + **Docker Compose** 容器化部署
- **Redis** 缓存和任务队列（可选）

## 🚀 快速开始

### 本地开发

1. **启动后端**
```bash
# 安装Python依赖
pip install -r requirements.txt

# 启动FastAPI服务
cd backend
python run.py
```

2. **启动前端**
```bash
# 安装Node.js依赖
cd frontend
npm install

# 启动Vite开发服务器
npm run dev
```

3. **访问应用**
- 前端界面：http://localhost:5173
- 后端API：http://localhost:8000
- API文档：http://localhost:8000/docs

### Docker部署

```bash
# 使用Docker Compose一键启动
docker-compose up --build
```

## 参考框架
https://github.com/QwenLM/Qwen-Image