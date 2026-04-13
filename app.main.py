from fastapi import FastAPI
import uvicorn
import os

app = FastAPI(title="gorurgari", description="Python App", version="1.0.0")


@app.get("/")
def root():
    return {"status": "ok", "message": "Python App is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/api/info")
def api_info():
    return {"app": "gorurgari", "language": "python", "framework": "fastapi"}


if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host=host, port=port, reload=False)