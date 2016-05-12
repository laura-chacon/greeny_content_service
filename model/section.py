import falcon
import boto
import os
from boto.s3.key import Key

s3 = boto.connect_s3(os.environ['ACCESS_KEY_ID'], 
                    os.environ['SECRET_ACCESS_KEY'])
content_bucket = s3.get_bucket('greeny-content')
k = Key(content_bucket)

class Section:
    def __init__(self, **kwargs):
        self.section_id = kwargs.get("section_id", None)
        self.display = kwargs.get("display", None)

    def get_section_id(self):
        return self.section_id

    def get_display(self):
        return self.display

def read_sections():
    k.key = 'sections.json'
    sections = k.get_contents_as_string()
    return sections
