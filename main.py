import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from src.api.routers import encoder

app_name: str = "Encoder Service"
app_description: str = "This is a simple service to convert mp3 files."

app = FastAPI(
    title=app_name,
    description=app_description,
    docs_url="/api",
)

app.include_router(encoder.router)

# CORS is required to run api simultaneously with website on local machine
# Allow localhost:8000 and 127.0.0.1:8000 to access the api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main():
    logging.info("run main")
    uvicorn.run(app, port=8002)


@app.get("/")
def rootreq():
    return {"home"}


@app.get("/health")
def health(request: Request):
    request.headers.get("X-Correlation-ID", default="not set")


if __name__ == "__main__":
    main()
