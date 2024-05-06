import os
import boto3
from dotenv import load_dotenv
from fastapi import UploadFile

load_dotenv()

aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')

s3 = boto3.client(
    "s3",
    aws_access_key_id = aws_access_key_id,
    aws_secret_access_key = aws_secret_access_key
)

def upload_to_s3(file:UploadFile, uploader:str):
    filename = file.filename
    s3.upload_fileobj(
        file.file,
        'with-you',
        f"{uploader}/{file.file}",
    )
    return f"https://with-you.s3.ap-northeast-2.amazonaws.com/{uploader}/{filename}"
    