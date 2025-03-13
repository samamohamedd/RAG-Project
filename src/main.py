from fastapi import FastAPI # type: ignore
from routes import base # type: ignore
from dotenv import load_dotenv  # type: ignore

load_dotenv(".env")

app = FastAPI()

app.include_router(base.base_router)
