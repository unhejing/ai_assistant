from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from loguru import logger
import os
from PIL import Image
from io import BytesIO

router = APIRouter(prefix="/api/images", tags=["images"])


class Txt2ImgRequest(BaseModel):
    prompt: str
    seed: Optional[int] = None
    steps: int = 30
    guidance_scale: float = 7.5
    width: int = 512
    height: int = 512


@router.post("/txt2img")
def txt2img(req: Txt2ImgRequest):
    """
    文生图接口（占位实现）：返回一张纯色图，模拟生成流程
    后续可替换为实际的Diffusers或Qwen-Image模型调用
    返回: { image_path: '/generated/placeholder.png' }
    """
    logger.info(f"Generating image with prompt: {req.prompt}")

    # 生成占位图像（可替换为真实模型推理）
    img = Image.new("RGB", (req.width, req.height), color=(73, 109, 137))
    output_dir = "generated"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "placeholder.png")
    img.save(file_path)

    # 返回可通过前端代理访问的绝对路径
    return {"image_path": f"/generated/placeholder.png"}


@router.post("/img2img")
def img2img(file: UploadFile = File(...), prompt: str = Form("")):
    """
    图生图接口（占位实现）：回传上传的图像路径
    后续可替换为真实的图生图模型推理
    返回: { image_path: '/uploads/xxx.png' }
    """
    output_dir = "uploads"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return {"image_path": f"/uploads/{file.filename}", "prompt": prompt}