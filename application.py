#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from url import *

settings = dict(
    debug=True,
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static")
    )

application = tornado.web.Application(
    handlers=admin_url + frontend_url,
    **settings
    )
