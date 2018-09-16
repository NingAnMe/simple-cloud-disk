#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/15
@Author  : AnNing
"""
from django.urls import path

from . import views

app_name = 'video'
urlpatterns = [
    # ex: /video/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /video/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /video/5/play/
    path('<int:pk>/play/', views.PlayView.as_view(), name='play'),
]
