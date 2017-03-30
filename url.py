#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.frontend.index import *

url = [
    (r'/', IndexHandler),
    (r'/about_us/', AboutUsHandler),
    (r'/international_projects/', InternationalProjectsHandler),
    (r'/contact_us/', ContactUsHandler),
    (r'/slabs/', SlabsHandler),
    (r'.*', PageNotFoundHandler),
]
