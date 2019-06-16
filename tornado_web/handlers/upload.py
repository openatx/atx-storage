# coding: utf-8
#

import hashlib
import os
import urllib

from tornado.web import StaticFileHandler, RequestHandler


class UploadItemHandler(StaticFileHandler):
    async def get(self, path, include_body=True):
        _, ext = os.path.splitext(path)
        hash = path.split("/")[0]
        abspath = os.path.join(ext[1:], hash+".raw")
        await super().get(abspath, include_body)


class UploadListHandler(RequestHandler):
    def get(self):
        pass

    def post(self):
        upload_dir = os.path.join(os.getcwd(), "uploads")
        urls = []
        for meta in self.request.files.get('file', None):
            filename = meta['filename']
            # print(filename)
            # print("Length:", len(meta['body']))

            basename, ext = os.path.splitext(filename)
            # print("ext:", ext)
            ext = ext.lstrip(".") or "unknown"
            filename = basename + "."+ext

            m = hashlib.md5()
            m.update(meta['body'])
            hash = m.hexdigest()

            target_path = os.path.join(upload_dir, ext, hash+".raw")
            os.makedirs(os.path.dirname(target_path), exist_ok=True)

            with open(target_path, "wb") as f:
                f.write(meta['body'])

            file_url = "/".join([self.request.full_url(),
                                 hash, urllib.parse.quote(filename)])
            urls.append(file_url)

        self.write({
            "urls": urls
        })
