# -*- coding: utf-8 -*-

"""
Create at 16/12/13
"""

__author__ = 'TT'

from tornado.web import RequestHandler
# from sqlalchemy.exc import SQLAlchemyError


class Index(RequestHandler):
    """"""

    def get(self, *args, **kwargs):
        """"""
        self.render('index.html')
