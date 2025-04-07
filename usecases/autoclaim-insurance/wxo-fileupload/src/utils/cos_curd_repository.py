from utils.cos_client import get_cos_client
from io import BytesIO


def upload_bytes_to_cos(data_bytes: bytes, bucket_name: str, file_key: str, content_type: str = "application/octet-stream"):
    try:
        cos_client = get_cos_client()
        file_obj = BytesIO(data_bytes)  # Wrap bytes in BytesIO

        cos_client.put_object(
            Bucket=bucket_name,
            Key=file_key,
            Body=data_bytes,
            ContentType=content_type  # Specify correct MIME type
        )

        print(f"Successfully uploaded {file_key} to {bucket_name}")

    except Exception as e:
        print(f"Failed to upload {file_key}: {str(e)}")
        raise


def read_object_from_cos(file_key: str, bucket_name: str):
    try:
        cos_object = get_cos_client().get_object(Bucket=bucket_name, Key=file_key)
        data = cos_object['Body'].read()
        return data
    except Exception as ex:
        print(
            f"Error: An error occurred while reading file from COS Bucket.The error is {ex}")
        return None