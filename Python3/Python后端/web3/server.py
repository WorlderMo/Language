# -*- coding: utf-8 -*-
# @Date    : 2018-08-21 21:09:55
# @Author  : mohailang (1198534595@qq.com)

import socket
import urllib.parse

from web3.utils import log

from web3.routes import route_static
from web3.routes import route_dict


class Request(object):
    """定义一个 class 用于保存请求的数据"""

    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.query = {}
        self.body = ''

    def form(self):
        """
        form 函数用于把 body 解析为一个字典并返回
        body 的格式如下：a=b&c=d&e=1
        """
        # 还原为字符串
        body = urllib.parse.unquote(self.body)
        args = body.split('&')
        f = {}
        for arg in args:
            k, v = arg.split('=')
            f[k] = v
        return f


request = Request()


def error(request, code=404):
    """
    根据 code返回不同的错误响应
    目前只有404
    """
    e = {
        404: b'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>NOT FOUND</h1>',
    }
    return e.get(code, b'')


def parsed_path(path):
    """
    用于把 path 和 query分离
    message=hello&author=gua
    {
        'message': 'hello',
        'author': 'gua',
    }
    """
    index = path.find('?')
    if index == -1:
        return path, {}
    else:
        path, query_string = path.split('?', 1)
        args = query_string.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = v
        return path, query


def response_for_path(path):
    path, query = parsed_path(path)
    request.path = path
    request.query = query
    log('path and query', path, query)
    """
    根据 path 调用相应的处理函数
    没有处理的 path 会返回404
    """
    r = {
        '/static': route_static,
    }
    r.update(route_dict)
    response = r.get(path, error)
    return response(request)


def run(host='', port=30000):
    """启动服务器"""
    log('start at {}:{}'.format(host, port))
    with socket.socket() as s:
        s.bind((host, port))
        while True:
            # 监听 接受 读取请求数据 解码成字符串
            s.listen(5)
            connection, address = s.accept()
            r = connection.recv(10000)
            r = r.decode('utf-8')
            log('原始请求', r)
            if len(r.split()) < 2:
                continue
            path = r.split()[1]
            request.method = r.split()[0]
            request.body = r.split('\r\n\r\n', 1)[1]
            response = response_for_path(path)
            connection.sendall(response)
            connection.close()


if __name__ == '__main__':
    config = dict(
        host='',
        port=30000,
    )
    run(**config)
