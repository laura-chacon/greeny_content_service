import falcon, content_service

api = application = falcon.API()
content_service = content_service.Resource()
