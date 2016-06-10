# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse


# 引入我们创建的表单类
from .form import AddForm


def index(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据
        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})


def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return JsonResponse(c, safe=False)


def to_add(request):
    return render(request, 'index2.html')


def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django',
                 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)
