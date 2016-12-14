# -*- coding: utf-8 -*-

"""
Create at 16/12/13
"""

__author__ = 'TT'

# 星座的dict，用来根据生日计算星座的。根据月份获取一个tuple，再比较日，大于就取index的1，否则就是index的-1
constellation_dict = {
    '01': (19, u'水瓶座', u'摩羯座'), '02': (18, u'双鱼座', u'水瓶座'),
    '03': (20, u'白羊座', u'双鱼座'), '04': (19, u'金牛座', u'白羊座'),
    '05': (20, u'双子座', u'金牛座'), '06': (21, u'巨蟹座', u'双子座'),
    '07': (22, u'狮子座', u'巨蟹座'), '08': (22, u'处女座', u'狮子座'),
    '09': (22, u'天秤座', u'处女座'), '10': (23, u'天蝎座', u'天秤座'),
    '11': (22, u'射手座', u'天蝎座'), '12': (21, u'摩羯座', u'射手座'),
}

AppID = 'wx094dee6d870e58ab'
AppSecret = '6b96aa12956ce3b964844410ea8d5272'
EncodingAESKey = 'Ji5DTTxV4aEIcBIs3mHvkhyKNQiKr3thREULHuoAiOf'
token = 'tt19890215'
wx_redirect_url = 'http://api.duanyong.wang/wx/userinfo'


class Config(object):
    """"""

    def __init__(self, env=None):
        """
        初始化配置文件，区分测试域名和生产域名，数据库连接等等信息
        """
        if env == 'test':
            self.test_conf()
        elif env == 'production':
            self.production_conf()
        elif env == 'tt':
            self.tt_conf()
        else:  # if env is None or env == 'dev':
            # debug mode
            self.debug = False

            # mysql config
            self.mysql_user = 'root'
            self.mysql_host = '127.0.0.1'
            self.mysql_passwd = '123'
            self.mysql_db = 'eileen'
            self.mysql_port = '3306'
            self.mysql_echo = False
            # redis config
            self.redis_host = '127.0.0.1'
            self.redis_port = '6379'
            self.redis_passwd = ''

    def tt_conf(self):
        """"""
        # debug mode
        self.debug = False

        # mysql config
        self.mysql_user = 'root'
        self.mysql_host = '127.0.0.1'
        self.mysql_passwd = '123'
        self.mysql_db = 'eileen'
        self.mysql_port = '3306'
        self.mysql_echo = False
        # redis config
        self.redis_host = '127.0.0.1'
        self.redis_port = '6379'
        self.redis_passwd = ''

    def test_conf(self):
        """"""
        # debug mode
        self.debug = False

        # mysql config
        self.mysql_user = 'root'
        self.mysql_host = '127.0.0.1'
        self.mysql_passwd = '123'
        self.mysql_db = 'eileen'
        self.mysql_port = '3306'
        self.mysql_echo = False
        # redis config
        self.redis_host = '127.0.0.1'
        self.redis_port = '6379'
        self.redis_passwd = ''

    def production_conf(self):
        """"""
        # debug mode
        self.debug = False

        # mysql config
        self.mysql_user = 'root'
        self.mysql_host = '127.0.0.1'
        self.mysql_passwd = '123'
        self.mysql_db = 'eileen'
        self.mysql_port = '3306'
        self.mysql_echo = False
        # redis config
        self.redis_host = '127.0.0.1'
        self.redis_port = '6379'
        self.redis_passwd = ''


