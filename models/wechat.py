# -*- coding: utf-8 -*-

"""
Create at 16/12/14
"""

__author__ = 'TT'
from urllib import quote
import requests
import json


AppID = 'wx094dee6d870e58ab'
AppSecret = '6b96aa12956ce3b964844410ea8d5272'
EncodingAESKey = 'Ji5DTTxV4aEIcBIs3mHvkhyKNQiKr3thREULHuoAiOf'
token = 'tt19890215'


class HttpClient(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = requests.Session()

        return cls._instance

client = HttpClient()


class WeChat(object):
    """微信授权信息"""
    code = None
    openid = None
    access_token = None
    user_info = None
    data = None
    timeout = 10
    response_type = 'code'
    scope = 'snsapi_userinfo'
    redirect_uri = 'http://api.duanyong.wang/wx/userinfo'

    def build_uri(self, params):
        keys = params.keys()
        keys.sort()

        _values = []
        for k in keys:
            v = params[k]
            if not v:
                continue

            v = v.encode('utf8') if isinstance(v, unicode) else v
            _values.append('{0}={1}'.format(k, v))

        return '&'.join(_values)

    def create_code_url(self):
        data = dict(
            appid=AppID,
            redirect_uri=quote(self.redirect_uri),
            response_tyep=self.response_type,
            scope=self.scope,
            state='1#wechat_redirect'
        )
        uri = self.build_uri(data)
        return 'https://open.weixin.qq.com/connect/oauth2/authorize?' + uri

    def create_access_token_url(self):
        data = dict(
            appid=AppID,
            secret=AppSecret,
            code=self.code,
            grant_type='authorization_code',
        )
        uri = self.build_uri(data)
        return 'https://api.weixin.qq.com/sns/oauth2/access_token?' + uri

    def create_user_info_url(self):
        data = dict(
            access_token=self.get_access_token(),
            openid=self.openid,
            lang='zh_CN',
        )
        uri = self.build_uri(data)
        return 'https://api.weixin.qq.com/sns/userinfo?' + uri

    def get_access_token(self):
        # 向微信提交以获取access_token
        url = self.create_access_token_url()
        try:
            data = client.get(url, timeout=self.timeout)
            self.access_token = json.loads(data.text)['access_token']
            self.openid = json.load(data.text)['openid']
        except Exception, e:
            print('request wx access token fail: {}'.format(e))

        return self.access_token

    def get_user_info(self):
        url = self.create_user_info_url()
        try:
            data = client.get(url, timeout=self.timeout)
            self.user_info = json.loads(data.content)
        except Exception, e:
            print('request wx access token fail: {}'.format(e))

        return self.user_info
