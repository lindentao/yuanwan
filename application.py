#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tornado.web

import url

settings = dict(
    debug=True,
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static")
    )

application = tornado.web.Application(
    handlers=url,
    **settings
    )
