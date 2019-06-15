# coding: utf-8

import os
from .handlers import main
from .handlers.upload import UploadListHandler, UploadItemHandler

urlpatterns = [
    (r"/", main.IndexHandler),
    (r"/uploads", UploadListHandler),
    (r"/uploads/(.*)", UploadItemHandler, {
        "path": os.path.join(os.getcwd(), "uploads")}),
]
