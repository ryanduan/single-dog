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
        data = dict(
            redirect_url='https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx094dee6d870e58ab&redirect_uri=http%3A%2F%2Fapi.duanyong.wang%2Fwx%2Fuserinfo&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect'
        )
        self.render('index.html', **data)
