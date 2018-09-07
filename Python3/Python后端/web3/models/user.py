# -*- coding: utf-8 -*-
# @Date    : 2018-08-28 13:02:34
# @Author  : mohailang (1198534595@qq.com)

from web3.models import Model


class User(Model):
    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    def validate_login(self):
        return self.username == 'hailang' and self.password == '123'

    def validate_register(self):
        return len(self.username) > 2 and len(self.password) > 2
