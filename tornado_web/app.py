# coding: utf-8
#

import os
from tornado.web import Application

from .urls import urlpatterns


def make_app(**settings):
    settings.update({
        "template_path": "templates",
        "static_path": "static",
        "cookie_secret": os.environ.get("SECRET", "SECRET:_"),
        "login_url": "/login",
        "websocket_ping_interval": 10,
    })
    return Application(urlpatterns, **settings)
