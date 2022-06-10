import boto3
import botocore
import os
import uuid
import base64
import time

BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"https://{BUCKET_NAME}.s3.amazonaws.com/"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

s3 = boto3.client(
   "s3",
   aws_access_key_id=os.environ.get("S3_KEY"),
   aws_secret_access_key=os.environ.get("S3_SECRET")
)

s3resource = boto3.resource(
    "s3",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET")
)


def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"

def current_milli_time_str():
    return str(round(time.time() * 1000))

def upload_base64_to_s3(image_base64):
    typeAndData = image_base64.split(",", 1)
    ext = typeAndData[0].split("/")[1].split(";")[0]
    file_name_with_extention = current_milli_time_str() + "." + ext
    obj = s3resource.Bucket(BUCKET_NAME).Object(file_name_with_extention)
    obj.put(Body=base64.b64decode(typeAndData[1]))
    #get object url
    location = "us-west-1"
    object_url = "https://%s.s3-%s.amazonaws.com/%s" % (BUCKET_NAME, location, file_name_with_extention)
    return object_url

def upload_file_to_s3(file, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        # in case the our s3 upload fails
        return {"errors": str(e)}

    return {"url": f"{S3_LOCATION}{file.filename}"}
