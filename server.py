#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from application import application

if __name__ == "__main__":
    application.listen(8090)
    tornado.ioloop.IOLoop.current().start()

# http: // www.goldea.com /