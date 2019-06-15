# coding: utf-8
#

import argparse
import socket
from logzero import logger
from tornado.ioloop import IOLoop
from tornado.log import enable_pretty_logging
from tornado.httpserver import HTTPServer
from tornado_web.app import make_app


def current_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 53))
    try:
        return s.getsockname()[0]
    finally:
        s.close()


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-p", "--port", default=4000, type=int, help="listen port")
    parser.add_argument("-d", "--debug", action="store_true", help="enable debug")
    parser.add_argument("-X", "--xheaders", action="store_true", help="retrive ip from X-Real-Ip/X-Forwarded-For")
    args = parser.parse_args()
    app = make_app()

    enable_pretty_logging()

    server = HTTPServer(app, xheaders=args.xheaders)
    server.listen(args.port)
    logger.info("listen on port http://%s:%d", current_ip(), args.port)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()


if __name__ == "__main__":
    main()
