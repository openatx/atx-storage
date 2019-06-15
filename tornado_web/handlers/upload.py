# coding: utf-8
#

from tornado.web import StaticFileHandler, RequestHandler


class UploadItemHandler(StaticFileHandler):
    async def get(self, path, include_body=True):
        filepath = self.get_absolute_path(self.root, path)
        await super().get(path.include_body)


class UploadListHandler(RequestHandler):
    def get(self):
        pass
