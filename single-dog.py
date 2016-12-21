# -*- coding: utf-8 -*-

"""
Create at 16/12/13
"""

__author__ = 'TT'

import os
import tornado.options
import tornado.ioloop
from tornado.options import options
import tornado.web
from tornado.httpserver import HTTPServer
from controllers.index import Index, Index1
from controllers.wx import WX, WXUser


class Application(tornado.web.Application):
    """"""

    def __init__(self):
        urls = [
            (r'/?', Index),
            (r'/wx/comment/?', WX),
            (r'/wx/userinfo.html/?', WXUser),
            (r'/index1/?', Index1),
        ]

        settings = dict(
            xsrf_cookies=False,
            debug=False,
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
        )

        tornado.web.Application.__init__(self, urls, **settings)

# if __name__ == '__main__':
#     options.define(name='config', default='tt')
#     options.define(name='port', default=31833)
#     options.define(name='process', default=2)
#
#     tornado.options.parse_command_line()
#     app = Application()
#     app.config = options.config
#
#     server = HTTPServer(app)
#     server.bind(int(options.port))
#     server.start(num_processes=int(options.process))
#     tornado.ioloop.IOLoop.instance().start()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = Application()
    app.listen(31833)
    tornado.ioloop.IOLoop.current().start()
