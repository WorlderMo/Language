# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
import json
# 引入用户账户模型
from users.models import User


def index(request):
    return render(request, 'basemain.html')


def basemain(request):
    return render(request, "basemain.html")


def accounts_profile(request):
    if request.method == 'POST':
        # 得到用户信息体
        a = json.loads(request.body)
        print(a)
        # 引入用户账户模型
        b = User.objects.get(email=request.user.email)
        # 修改信息
        b.name = a['name']
        b.phone = a['phone']
        b.sex = a['sex']
        # 保存
        b.save()
    return render(request, 'accounts_profile.html')
