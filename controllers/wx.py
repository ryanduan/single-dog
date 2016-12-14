# -*- coding: utf-8 -*-

"""
Create at 16/12/13

AppID = 'wx094dee6d870e58ab'
AppSecret = '6b96aa12956ce3b964844410ea8d5272'
EncodingAESKey = 'Ji5DTTxV4aEIcBIs3mHvkhyKNQiKr3thREULHuoAiOf'
token = 'tt19890215'

https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx094dee6d870e58ab&redirect_uri=http%3A%2F%2Fapi.duanyong.wang%2Fwx%2Fuserinfo&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect

"""

__author__ = 'TT'

from tornado.web import RequestHandler
from models.config import token
import hashlib
from models.wechat import WeChat

# wx_redirect_url = urlencode('http://api.duanyong.wang/wx/userinfo')
wx_redirect_url = 'http%3A%2F%2Fapi.duanyong.wang%2Fwx%2Fuserinfo'


class WX(RequestHandler):
    """
    pass
    """

    def get(self, *args, **kwargs):
        """"""
        signature = self.get_argument('signature', '')
        timestamp = self.get_argument('timestamp', '')
        nonce = self.get_argument('nonce', '')
        echostr = self.get_argument('echostr', '')
        sign_list = [token, timestamp, nonce]
        sign_list.sort()
        sha1_str = hashlib.sha1()
        map(sha1_str.update, sign_list)
        hashcode = sha1_str.hexdigest()
        if hashcode == signature:
            self.write(echostr)
        else:
            # 校验没通过，不是还是要确认的
            print 'hashcode not pass'
            self.write(echostr)


class WXUser(RequestHandler):
    """"""

    def get(self, *args, **kwargs):
        """"""

        code = self.get_argument('code', '')
        wc = WeChat()
        wc.code = code
        user_info = wc.get_user_info()
        print user_info
        self.redirect('http://eileen.duanyong.wang/index')
