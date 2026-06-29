from fastapi import FastAPI
from routes.progress.router import router as progress_router

app = FastAPI()

def main() -> None:
    app.include_router(progress_router, prefix='/progress')


if __name__ == "__main__":
    main()
