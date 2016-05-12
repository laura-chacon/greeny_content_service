import falcon
import sys
import json
import requests
from model.action_types import ActionTypes
import model.action_types

class GetActionTypesController(object):
    def on_get(self, req, resp, section):
        action_types = model.action_types.read_action_types(section)
        resp.body = action_types
        resp.status = falcon.HTTP_200
