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

class ActionTypes:
    def __init__(self, **kwargs):
        self.action_types_id = kwargs.get("action_types_id", None)
        self.display = kwargs.get("display", None)

def read_action_types(section):
    if(section == "food"):
        response = client.get_object(
            Bucket='greeny-content',
            Key='food_actions_type.json'
        )
    elif(section == "water"):
        response = client.get_object(
            Bucket='greeny-content',
            Key='water_actions_type.json'
        )
    elif(section == "transportation"):
        response = client.get_object(
            Bucket='greeny-content',
            Key='transportation_actions_type.json'
        )
    else:
        response = client.get_object(
            Bucket='greeny-content',
            Key='heating_cooling_actions_type.json'
        )
    return response['Body'].read()
