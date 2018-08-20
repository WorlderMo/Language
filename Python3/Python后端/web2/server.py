# -*- coding: utf-8 -*-
# @Date    : 2018-08-18 16:23:45
# @Author  : mohailang (1198534595@qq.com)
# server.py是一个简单的web后端框架
import socket


def log(*args, **kwargs):
    """用这个 log 替代 print"""
    print('log', *args, **kwargs)


def route_index():
    """主页的处理函数，返回主页的响应"""
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
    body = '<h1>Hello mohailang</h1>'
    r = header + body
    return r.encode(encoding='utf-8')


def page(name):
    with open(name, encoding='utf-8') as f:
        return f.read()


def route_msg():
    """msg 页面的处理函数"""
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
    body = page('msg.html')
    r = header + body
    return r.encode(encoding='utf-8')


def route_image():
    """图片的处理函数，读取图片并生成响应返回"""
    with open('doge.gif', 'rb') as f:
        header = b'HTTP/1.1 200 OK\r\nContent-Type: image/gif\r\n\r\n'
        img = header + f.read()
        return img


def error(code=404):
    """根据 code 返回不同的错误响应"""
    e = {
        404: b'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>NOT FOUND</h1>',
    }
    return e.get(code, b'')


def response_for_path(path):
    """
    根据 path 调用相应的处理函数
    没有处理的 path 返回404
    """
    r = {
        '/': route_index,
        '/doge.gif': route_image,
        '/msg': route_msg,
    }
    response = r.get(path, error)
    return response()


def run(host='', port=30000):
    """启动服务器"""
    with socket.socket() as s:
        s.bind((host, port))
        # 无限循环来处理请求
        while True:
            # 监听 接受 读取请求数据 解码成字符串
            s.listen(5)
            connection, address = s.accept()
            request = connection.recv(1024)
            log('raw', request)
            request = request.decode('utf-8')
            log('request{}'.format(request))
            try:
                # 因为 Chrome会发送空请求导致 split 得到空 list
                # 所以这里用 try 防止程序崩溃
                path = request.split()[1]
                # 用 response_for_path 函数得到 path 对应的响应内容
                response = response_for_path(path)
                # 把响应数据发送给客户端
                connection.sendall(response)
            except Exception as e:
                log('error', e)
            connection.close()


def main():
    # 生成配置并且运行程序
    config = dict(
        host='',
        port=30000,
    )
    run(**config)


if __name__ == '__main__':
    main()
