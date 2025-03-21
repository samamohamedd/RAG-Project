from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from models import ResponseSignal
import os
import aiofiles
import logging

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/data",
    tags=["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")

async def upload_data(project_id: str,
                        file: UploadFile,
                        app_settings: Settings = Depends(get_settings)):
    
    # file validation 
    data_controller = DataController()
    is_valid, result_massage = data_controller.validate_file(file=file)

    if not is_valid :
        return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"signal" : result_massage}
            )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = data_controller.generate_unique_filename(
        original_file_name=file.filename,
        project_id=project_id
        )

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while Uploading File {e}")

        return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"signal" : ResponseSignal.FILE_UPLOAD_FAILED.value}
            )

    return JSONResponse(
        content={
            "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value
        }
    )


