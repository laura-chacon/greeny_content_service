import falcon
import sys
import json
import requests
from model.section import Section
import model.section

class GetSectionsController(object):
    def on_get(self, req, resp):
        sections = model.section.read_sections()
        resp.body = sections
        resp.status = falcon.HTTP_200
