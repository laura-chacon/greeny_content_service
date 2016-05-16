import falcon
import boto
import os
from boto.s3.key import Key
import boto3

client = boto3.client(
    's3',
    region_name='eu-west-1',
    aws_access_key_id=os.environ['ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['SECRET_ACCESS_KEY']
)

class Section:
    def __init__(self, **kwargs):
        self.section_id = kwargs.get("section_id", None)
        self.display = kwargs.get("display", None)

    def get_section_id(self):
        return self.section_id

    def get_display(self):
        return self.display

def read_sections():
    response = client.get_object(
        Bucket='greeny-content',
        Key='sections.json'
    )
    return response['Body'].read()
