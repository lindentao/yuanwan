#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.ioloop

from application import application

if __name__ == "__main__":
    application.listen(8090)
    tornado.ioloop.IOLoop.current().start()
