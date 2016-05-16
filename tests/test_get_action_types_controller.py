import falcon
import falcon.testing as testing
import uuid
import main
import json
from types import UnicodeType
import six

class TestSectionsController(testing.TestBase):
    def before(self):
        self.api = main.create_api()

    def test_success_get_sections(self):
        section_id = "food"
        body = self.req(section_id)
        food_action_types = json.loads(body)
        food_action_types = food_action_types['action_types']
        self.assertEqual(4, len(food_action_types))
        self.assertEqual(self.srmock.status, falcon.HTTP_200)

    def req(self, section):
        headers = [('Accept', 'application/json'),
                       ('Content-Type', 'application/json'),]
        return self.simulate_request('/sections/' + section + '/actions',
                                     headers=headers,
                                     decode='utf-8',
                                     method="GET",
                                     body="")
