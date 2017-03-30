#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from optsql.models import *

class BaseHandler(tornado.web.RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')

class AboutUsHandler(BaseHandler):
    def get(self):
        self.render('about_us.html')

class InternationalProjectsHandler(BaseHandler):
    def get(self):
        self.render('international_projects.html')

class ContactUsHandler(BaseHandler):
    def get(self):
        self.render('contact_us.html')

class SlabsHandler(BaseHandler):
    def get(self):
        page = int(self.get_argument('page', 1))
        if page <= 0:
            page = 1
        rows_per_page = 12

        qset = Product.objects().order_by('-updated_at')
        objs = qset.skip((page - 1) * rows_per_page).limit(rows_per_page)
        total = qset.count()
        count = total / rows_per_page if (total % rows_per_page == 0) else total / rows_per_page + 1
        if page >= count:
            page = count
        page_info = {
            'rows_per_page': rows_per_page,
            'total': total,
            'page_count': count,
            'page_current': page,
            'page_prev': page - 1,
            'page_next': page + 1,
        }
        self.render('slabs.html', objs=objs, page=page_info,)

class PageNotFoundHandler(BaseHandler):
    def get(self):
        self.render('error.html')


