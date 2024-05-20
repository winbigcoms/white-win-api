import os
import boto3
from dotenv import load_dotenv
from model.withyou import PostImg
from fastapi import UploadFile
import requests
from io import BytesIO
from botocore.exceptions import NoCredentialsError
from botocore.config import Config

load_dotenv()

aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')

my_config = Config(
    region_name='ap-northeast-2',
    signature_version='s3v4'
)


s3 = boto3.client(
    "s3",
    aws_access_key_id = aws_access_key_id,
    aws_secret_access_key = aws_secret_access_key,
    config = my_config
)

def make_presign_url(uploader):
    try:
        response = s3.generate_presigned_url('put_object',
                                            Params={
                                                'Bucket': "with-you",
                                                'Key': f"with-you/{uploader}"},
                                            ExpiresIn=3600)
    except NoCredentialsError:
        print("no cred")
        return None

    return response

def upload_to_s3(file:PostImg, uploader:str):
    filename = file.filename
    imageDate = base64.b64decode(file.base64)
    s3.upload_fileobj(
        BytesIO(imageDate),
        'with-you',
        f"{uploader}/{file.filename}",
    )
    return f"https://with-you.s3.ap-northeast-2.amazonaws.com/{uploader}/{filename}"
    