# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""zqxt_form2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tools import views as tools_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^to_add/', tools_views.to_add),
    url(r'^ajax_list/$', tools_views.ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', tools_views.ajax_dict, name='ajax-dict'),
    url(r'^add/', tools_views.add, name='add'),
    url(r'^$', tools_views.index, name='home'),
]
