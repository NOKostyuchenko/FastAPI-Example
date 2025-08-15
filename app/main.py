from fastapi import FastAPI
from uvicorn import run

from api import base_router

app = FastAPI(docs_url="/swagger")

app.include_router(base_router)

if __name__ == "__main__":
    run(app="main:app", reload=True, port=8001)