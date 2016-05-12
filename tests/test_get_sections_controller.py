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
        body = self.req()
        sections = json.loads(body)
        sections = sections['sections']
        self.assertEqual(4, len(sections))
        self.assertEqual(self.srmock.status, falcon.HTTP_200)

    def req(self):
        headers = [('Accept', 'application/json'),
                       ('Content-Type', 'application/json'),]
        return self.simulate_request('/sections',
                                     headers=headers,
                                     decode='utf-8',
                                     method="GET",
                                     body="")
