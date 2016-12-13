# -*- coding: utf-8 -*-

"""
Create at 16/12/13
"""

__author__ = 'TT'

from tornado.web import RequestHandler
from sqlalchemy.exc import SQLAlchemyError
from models.config import AppID, AppSecret, EncodingAESKey, token


class WX(RequestHandler):
    """"""

    def get(self, *args, **kwargs):
        self.write("test")
