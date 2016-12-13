# -*- coding: utf-8 -*-

"""
Create at 16/12/13
"""

__author__ = 'TT'

from dao import Base
from sqlalchemy import Column, Integer, String, DateTime
import datetime
import time


class Image(Base):
    """"""
    __tablename__ = 'image'

    image_id = Column(Integer, primary_key=True)
    uri = Column(String(200), nullable=False, unique=True)
    create_at = Column(Integer, nullable=True, default=lambda: int(time.time()))
    show_time = Column(Integer, nullable=False, default=0)
    show_date = Column(DateTime, nullable=False, default=lambda: datetime.datetime.now())
    event_id = Column(Integer, nullable=True)
