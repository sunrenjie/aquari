#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from school.models import App


a = App(slug='weixin', name='WeiXin', info=u'微信，超过5亿人使用的应用', summary=u'微信，超过5亿人使用的应用',
        category='social')

a.save()
b = App(slug='qq', name='手机QQ', info=u'手机QQ，只想与你更接近', summary=u'手机QQ，只想与你更接近',
        category='social')

b.save()
c = App(slug='com.mt.mtxx.mtxx', name=u'美图秀秀', info=u'重磅推出“增高”功能，瞬间拥有',
        summary=u'重磅推出“增高”功能，瞬间拥有', category='utility')
c.save()
