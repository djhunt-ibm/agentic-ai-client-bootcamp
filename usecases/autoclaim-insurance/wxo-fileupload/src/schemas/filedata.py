from fastapi import UploadFile
from pydantic import BaseModel
import base64


class FileData(BaseModel):
        filedata: str
        original_file_name: str
