# -*- coding: utf-8 -*-
# @Date    : 2018-08-21 23:40:30
# @Author  : mohailang (1198534595@qq.com)

import json

"""
json 是一种时下非常流行的数据格式
在 python 中可以方便地使用 json 格式序列化/反序列化字典或者列表
"""
from web3.utils import log


def save(data, path):
    """
    本函数把一个 dict或者 list 写入文件
    data 是 dict 或者 list
    path 是保存文件的路径
    """
    # indent 是缩进
    # ensure_ascii=False 用于保存中文
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        log('save', path, s, data)
        f.write(s)


def load(path):
    """
    本函数从一个文件中载入数据并转化为 dict或者 list
    path 是保存文件的路径
    """
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        log('load', s)
        return json.loads(s)


# Model 是用于存储数据的基类
class Model(object):
    @classmethod
    def db_path(cls):
        class_name = cls.__name__
        path = 'db/{}.txt'.format(class_name)
        return path

    @classmethod
    def new(cls, form):
        m = cls(form)
        return m

    @classmethod
    def all(cls):
        """得到一个类的所有存储的实例"""
        path = cls.db_path()
        models = load(path)
        ms = [cls.new(m) for m in models]
        return ms

    def save(self):
        """save 函数用于把一个 Model 的实例保存到文件中"""
        models = self.all()
        log('models', models)
        models.append(self)
        # __dict__是包含了对象所有属性和值的字典
        data = [m.__dict__ for m in models]
        path = self.db_path()
        save(data, path)

    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ['{}: {}'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} >\n'.format(class_name, s)
