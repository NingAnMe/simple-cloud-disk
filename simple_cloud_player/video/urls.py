#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/15
@Author  : AnNing
"""
from django.urls import path

from . import views

urlpatterns = [
    # ex: /video/
    path('', views.index, name='index'),
    # ex: /video/5/
    path('<int:video_id>/', views.detail, name='detail'),
    # ex: /video/5/play/
    path('<int:video_id>/play/', views.play, name='results'),
]
