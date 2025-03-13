from fastapi import FastAPI, APIRouter # type: ignore
import os

base_router = APIRouter(
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return{
        "app_name" : app_name,
        "app_version" : app_version
    }