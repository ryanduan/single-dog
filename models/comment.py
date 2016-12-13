# -*- coding: utf-8 -*-

"""
Create at 16/12/13
"""

__author__ = 'TT'

from dao import Base
from sqlalchemy import Column, Integer, DateTime, Text
import datetime
import time


class Comment(Base):
    """"""
    __tablename__ = 'comment'

    comment_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, default=0)
    content = Column(Text, nullable=True)
    create_at = Column(Integer, nullable=True, default=lambda: int(time.time()))
    show_time = Column(Integer, nullable=False, default=0)
    show_date = Column(DateTime, nullable=False, default=lambda: datetime.datetime.now())