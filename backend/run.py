import uvicorn

if __name__ == "__main__":
    # 启动FastAPI服务
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)