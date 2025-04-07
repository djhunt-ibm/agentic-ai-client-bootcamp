
import random
import string
from utils.cos_curd_repository import upload_bytes_to_cos
import os
from dotenv import load_dotenv
import base64
import imghdr
import magic
import zipfile
import tempfile

load_dotenv()
bucket_name = os.getenv("BUCKET_NAME", None)


def get_file_type_from_base64str(base64_string):

    # Remove Base64 prefix if present (e.g., "data:image/png;base64,")
    if "," in base64_string:
        base64_string = base64_string.split(",")[1]

    # Decode Base64 string to bytes
    file_bytes = base64.b64decode(base64_string)

    # Use imghdr to detect image type
    image_type = imghdr.what(None, file_bytes)

    # If imghdr detects webp, override it with manual checks
    if image_type == "webp":
        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(file_bytes)

        # Force PNG/JPG correction
        if "jpeg" in mime_type:
            return "image/jpg"
        else:
            return "image/png"

    # Use magic as a final check
    mime = magic.Magic(mime=True)
    return mime.from_buffer(file_bytes)


def save_file(base64_string: str, original_file_name: str):

    uploaded_files =[]
    try:
        # Remove Base64 prefix if present (e.g., "data:image/png;base64,")
        if "," in base64_string:
            base64_string = base64_string.split(",")[1]

        # Decode the Base64 string
        file_bytes = base64.b64decode(base64_string)

        filetype = get_file_type_from_base64str(base64_string)
        file_extenstion = filetype.split("/")[1]
        print(file_extenstion)
        if file_extenstion == 'plain':
            file_extenstion = 'txt'
        elif file_extenstion.endswith("wordprocessingml.document"):
            file_extenstion = "docx"
        elif file_extenstion.endswith("spreadsheetml.sheet"):
            file_extenstion = "xlsx"
        elif file_extenstion.endswith("presentationml.presentation"):
            file_extenstion = "pptx"
        elif filetype == "application/zip":
            return extract_and_upload_zip(file_bytes, bucket_name)
        #filename = f"{generate_code()}.{file_extenstion}"
        filename = f"{generate_code()}.{file_extenstion}"

        upload_bytes_to_cos(file_bytes, bucket_name, original_file_name, filetype)
        uploaded_files.append(original_file_name)
        return uploaded_files
    except Exception as ex:
        raise ex


def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def extract_and_upload_zip(zip_bytes, bucket_name):
    """
    Extracts ZIP file contents and uploads each extracted file to COS.
    """
    uploaded_files = []

    with tempfile.TemporaryDirectory() as temp_dir:
        zip_path = os.path.join(temp_dir, "uploaded.zip")

        # Save the ZIP file temporarily
        with open(zip_path, "wb") as f:
            f.write(zip_bytes)

        # Extract ZIP contents
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        # Upload each extracted file
        for root, dirs, files in os.walk(temp_dir):
            # Ignore hidden directories (like __MACOSX)
            dirs[:] = [d for d in dirs if not d.startswith(".")]

            for file_name in files:
                # Skip hidden files
                if file_name.startswith(".") or file_name == "uploaded.zip":
                    continue

                file_path = os.path.join(root, file_name)

                # Read file bytes
                with open(file_path, "rb") as f:
                    file_data = f.read()

                # Detect file type
                mime = magic.Magic(mime=True)
                file_type = mime.from_buffer(file_data)

                # Upload to COS
                upload_bytes_to_cos(file_data, bucket_name, file_name, file_type)
                uploaded_files.append(file_name)

    return uploaded_files