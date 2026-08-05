from dotenv import load_dotenv
from fastapi import FastAPI

from routes.progress.router import router as progress_router
from routes.progress.ready.router import router as progress_ready_router

load_dotenv()

app = FastAPI()

app.include_router(progress_router, prefix="/progress")
app.include_router(progress_ready_router, prefix="/progress/ready")
