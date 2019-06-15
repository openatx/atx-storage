# coding: utf-8
#

from tornado.web import RequestHandler
from tornado.escape import json_decode


class BaseRequestHandler(RequestHandler):
    pass
    

class IndexHandler(BaseRequestHandler):
    def get(self):
        self.write("Hello ATX-Storage")
