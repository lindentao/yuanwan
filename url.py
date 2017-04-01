#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.index import *
from handlers.admin import *

admin_url = [
    (r'/admin/', IndexHandler),
    (r'/admin/category', CategoryHandler),
]

frontend_url = [
    (r'/', IndexHandler),
    (r'/about_us/', AboutUsHandler),
    (r'/international_projects/', InternationalProjectsHandler),
    (r'/contact_us/', ContactUsHandler),
    (r'/slabs/', SlabsHandler),
    (r'.*', PageNotFoundHandler),
]

