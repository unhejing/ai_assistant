import os
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, List
from loguru import logger

# 模块化路由
from .routers import images, extensions

# 环境配置
API_PREFIX = "/"
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="AI Assistant Backend", version="0.1.0")

# 静态资源挂载，暴露生成图像与上传文件目录，以便前端直接访问
# 说明：这些目录用于承载模型生成的图片（generated）与用户上传的素材（uploads）
os.makedirs("generated", exist_ok=True)
os.makedirs("uploads", exist_ok=True)
app.mount("/generated", StaticFiles(directory="generated"), name="generated")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# CORS配置，允许前端访问
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含图像相关API
app.include_router(images.router, prefix=API_PREFIX)
# 扩展模块API
app.include_router(extensions.router, prefix=API_PREFIX)


@app.get("/health")
def health_check():
    """健康检查接口，返回服务状态"""
    return {"status": "ok"}