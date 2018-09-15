#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/15
@Author  : AnNing
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]