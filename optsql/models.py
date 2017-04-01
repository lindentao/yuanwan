#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# 初始化数据库连接，数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
engine = create_engine("mysql+pymysql://root:123456@localhost:13306/test_sql", encoding='utf-8', echo=False)

# 创建对象的基类:
Base = declarative_base()


class Article(Base):
    # 表的名字:
    __tablename__ = 't_article_info'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default='', unique=True)
    body = Column(Text, nullable=False)
    status = Column(SmallInteger, nullable=False, default=0)
    ctime = Column(DateTime, nullable=False, default=datetime.now())
    mtime = Column(DateTime, nullable=False, default=datetime.now())


class Category(Base):
    __tablename__ = 't_category_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default='', unique=True)
    ctime = Column(DateTime, nullable=False, default=datetime.now())
    goods = relationship('Goods')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<User(name='%s', ctime='%s')>" % (self.name, self.ctime)


class Goods(Base):
    __tablename__ = 't_goods_info'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('t_category_info.id'), nullable=False)
    name = Column(String(32), nullable=False, default='', unique=True)
    origin = Column(String(32), default='')
    color = Column(String(32), default='')
    material = Column(String(32), default='')
    size = Column(String(32), default='')
    ctime = Column(DateTime, nullable=False, default=datetime.now())
    mtime = Column(DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return "<Goods(name='%s', category_id='%s')>" % (self.name, self.category_id)


class GoodsImage(Base):
    __tablename__ = 't_goods_image'

    id = Column(Integer, primary_key=True)
    goods_id = Column(Integer, ForeignKey('t_goods_info.id'), nullable=False)
    image_id = Column(Integer, ForeignKey('t_image_info.id'), nullable=False)


class Image(Base):
    __tablename__ = 't_image_info'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default='')
    path = Column(String(64), nullable=False, default='')


if __name__ == "__main__":
    '''仅供测试models代码'''
    # 创建表，如果表存在则忽视
    Base.metadata.create_all(engine)
