import falcon
import boto
import os
from boto.s3.key import Key

s3 = boto.connect_s3(os.environ['ACCESS_KEY_ID'],
                    os.environ['SECRET_ACCESS_KEY'])
content_bucket = s3.get_bucket('greeny-content')
k = Key(content_bucket)

class ActionTypes:
    def __init__(self, **kwargs):
        self.action_types_id = kwargs.get("action_types_id", None)
        self.display = kwargs.get("display", None)

def read_action_types(section):
    if(section == "food"):
        k.key = 'food_actions_type.json'
    elif(section == "water"):
        k.key = 'water_actions_type.json'
    elif(section == "transportation"):
        k.key = 'transportation_actions_type.json'
    else:
        k.key = 'heating_cooling_actions_type.json'
    action_types = k.get_contents_as_string()
    return action_types
