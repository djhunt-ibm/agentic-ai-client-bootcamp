from fastapi import APIRouter, Body, UploadFile
from services import file_process_service
from schemas.filedata import FileData
router = APIRouter()


@router.post(path="/file/upload")
async def process_filestream(fileobj: FileData):
    try:
        response = await file_process_service.process_filestream(fileobj.filedata, fileobj.original_file_name)
    except Exception as ex:
        return {"error": str(ex)}

    return {
        "info": "success",
        "file_name": response
    }
