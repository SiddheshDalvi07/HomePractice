import boto3
s3_res= boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='',
    aws_secret_access_key=''
)

for item in s3_res.buckets.all():
    print(item)


s3_res.Bucket('mybuckkie').upload_file("sid.txt",Key="sid.txt")
