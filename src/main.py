from fastapi import FastAPI # type: ignore
from routes import base # type: ignore

app = FastAPI()

app.include_router(base.base_router)

