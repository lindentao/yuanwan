#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 #  @file       index.py
 #  @brief
    ---------------------------------------------------------
    功能简介    admin管理面板的处理函数
    ---------------------------------------------------------
 #  @version    1.0.0
 #  @author     LindenTao(lindentao@qq.com)
 #  @date       17/4/1 下午3:11

              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

import tornado.web
from optsql.models import *


class BaseHandler(tornado.web.RequestHandler):
    pass


class IndexHandler(BaseHandler):
    def get(self):
        self.render('admin/index.html')


class CategoryHandler(BaseHandler):
    def get(self):
        self.render('admin/category/show.html')
