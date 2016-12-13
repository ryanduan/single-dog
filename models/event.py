# # -*- coding: utf-8 -*-
#
# """
# Create at 16/12/13
# """
#
# __author__ = 'TT'
#
# from dao import Base
# from sqlalchemy import Column, Integer, String, DateTime, Text
# import datetime
# import time
#
#
# class Event(Base):
#     """"""
#     __tablename__ = 'event'
#
#     event_id = Column(Integer, primary_key=True)
#     title = Column(String(200), nullable=True)
#     content = Column(Text, nullable=True)
#     create_at = Column(Integer, nullable=True, default=lambda: int(time.time()))
#     show_time = Column(Integer, nullable=False, default=0)
#     show_date = Column(DateTime, nullable=False, default=lambda: datetime.datetime.now())
