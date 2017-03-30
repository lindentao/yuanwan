#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *
from datetime import datetime

from settings import *

connect(db_name, host=db_host)

class Category(Document):
    cid = StringField(primary_key=True, required=True, unique=True, max_length=8, verbose_name=u'分类ID')
    name = StringField(required=True, max_length=24, verbose_name=u'分类名称')
    type = StringField(required=True, max_length=8, verbose_name=u'分类类别')

    @property
    def products(self):
        '''| products | 产品列表 | List: [Product](#products) |  |  | |  |  |'''

        return Product.objects(category=self.pk)

materialChoice = (
    ('Real', u'Real wood'),
    ('Composite', u'Composite board'),
    )

stylelChoice = (
    ('European', u'European style '),
    ('Modern', u'Modern style'),
    ('Classical', u'Classical style'),
    )

class ProductPic(EmbeddedDocument):
    '''产品图片'''
    created_at = DateTimeField(required=True, default=datetime.now, verbose_name=u'创建时间')
    name = StringField(default=u'', max_length=32, verbose_name=u'名字')
    path = StringField(required=True, max_length=128, verbose_name=u'路径')

class Product(Document):
    category = ReferenceField(Category, required=True, verbose_name=u'类别', reverse_delete_rule=DENY)
    name = StringField(required=True, max_length=64, verbose_name=u'产品名称')
    material = StringField(max_length=16, choices=materialChoice, verbose_name=u'材料种类')
    pic = ListField(EmbeddedDocumentField(ProductPic), required=False, default=[], verbose_name=u'图片列表')
    style = StringField(max_length=16, choices=stylelChoice, verbose_name=u'风格种类')
    updated_at = DateTimeField(required=True, default=datetime.now, verbose_name=u'更新时间')


if __name__ == "__main__":
    '''仅供测试models代码'''
    # category1 = Category(cid='11', name='Entrance door', type='1')
    # category1.save()
    count = 0
    while (count<12):
        ppic1 = ProductPic(path='/static/images/201610221527244555.jpg')
        ppic2 = ProductPic(path='/static/images/201610221527383035.jpg')
        prod = Product(category='1', name=' Latest Design Wooden Door Interior Door Room Door', material='Real', style='European')
        prod.pic = [ppic1, ppic2]
        prod.save()
        count = count + 1
