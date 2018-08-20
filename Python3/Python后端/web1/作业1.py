# -*- coding: utf-8 -*-
# @Date    : 2018-08-15 22:42:57
# @Author  : mohailang (1198534595@qq.com)

import socket
import ssl

"""
作业 1 答案
===

附带了测试和 https 请求


资料:

一、使用 https
    1, https 请求的默认端口是 443
    2, https 的 socket 连接需要 import ssl
        并且使用 s = ssl.wrap_socket(socket.socket()) 来初始化

    试试用这个请求豆瓣电影 top250
    url = 'https://movie.douban.com/top250'

    你就能得到网页的 html 源代码
    然后保存为 html 文件 你就能用浏览器打开


二、HTTP 协议的 301 状态
    请求豆瓣电影 top250 (注意协议)
    http://movie.douban.com/top250
    返回结果是一个 301
    301 状态会在 HTTP 头的 Location 部分告诉你应该转向的 URL
    所以, 如果遇到 301, 就请求新地址并且返回
        HTTP/1.1 301 Moved Permanently
        Date: Sun, 05 Jun 2016 12:37:55 GMT
        Content-Type: text/html
        Content-Length: 178
        Connection: keep-alive
        Keep-Alive: timeout=30
        Location: https://movie.douban.com/top250
        Server: dae
        X-Content-Type-Options: nosniff

        <html>
        <head><title>301 Moved Permanently</title></head>
        <body bgcolor="white">
        <center><h1>301 Moved Permanently</h1></center>
        <hr><center>nginx</center>
        </body>
        </html>

https 的默认端口是 443, 所以你需要在 get 函数中根据协议设置不同的默认端口

"""


def parsed_url(url):
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u = url

    # 检查默认 path
    i = u.find('/')
    if i == -1:
        host = u
        path = '/'
    else:
        host = u[:i]
        path = u[i:]

    port_dict = {
        'http': 80,
        'https': 443,
    }
    port = port_dict[protocol]
    if ':' in host:
        h = host.split(':')
        host = h[0]
        port = int(h[1])
    return protocol, host, port, path


def socket_by_protocol(protocol):
    """根据协议返回一个 socket 实例"""
    if protocol == 'http':
        s = socket.socket()
    else:
        # https 协议需要使用ssl.wrap_scoket 包装原始的 socket
        s = ssl.wrap_socket(socket.socket())
    return s


def response_by_socket(s):
    response = b''
    buffer_size = 1024
    while True:
        r = s.recv(buffer_size)
        if len(r) == 0:
            break
        response += r
    return response


def parsed_response(r):
    header, body = r.split('\r\n\r\n', 1)
    h = header.split('\r\n')
    status_code = int(h[0].split()[1])

    headers = {}
    for line in h[1:]:
        k, v = line.split(': ')
        headers[k] = v
    return status_code, headers, body


def get(url):
    """用 get 请求 URL 并返回响应"""
    protocol, host, port, path = parsed_url(url)

    s = socket_by_protocol(protocol)
    s.connect((host, port))

    request = 'GET {} HTTP/1.1\r\nhost: {}\r\nConnection: close\r\n\r\n'.format(
        path, host)
    encoding = 'utf-8'
    s.send(request.encode(encoding))

    response = response_by_socket(s)
    r = response.decode(encoding)

    status_code, headers, body = parsed_response(r)
    if status_code == 301:
        url = headers['Location']
        return get(url)
    return status_code, headers, body


def main():
    url = 'http://movie.douban.com/top250'
    status_code, headers, body = get(url)
    print(status_code, headers, body)


def test_parsed_url():
    """测试函数"""
    http = 'http'
    https = 'https'
    host = 'g.cn'
    path = '/'
    test_items = [
        ('http://g.cn', (http, host, 80, path)),
        ('http://g.cn/', (http, host, 80, path)),
        ('http://g.cn:90', (http, host, 90, path)),
        ('http://g.cn:90/', (http, host, 90, path)),
        #
        ('https://g.cn', (https, host, 443, path)),
        ('https://g.cn:233/', (https, host, 233, path)),
    ]
    for item in test_items:
        url, expected = item
        u = parsed_url(url)
        # assert 是一个断言语句
        # 如果断言成功，条件成立，则通过测试，否则测试失败，中断程序报错
        e = "parsed_url ERROR, ({}) ({}) ({})".format(url, u, expected)
        assert u == expected, e  # 如果u==expected不成立，则输出 e的报错信息


def test_parsed_response():
    """测试是否能正确解析响应"""
    response = 'HTTP/1.1 301 Moved Permanently\r\n' \
        'Content-Type: text/html\r\n' \
        'Location: https://movie.douban.com/top250\r\n' \
        'Content-Length: 178\r\n\r\n' \
        'test body'
    status_code, header, body = parsed_response(response)
    assert status_code == 301
    assert len(list(header.keys())) == 3
    assert body == 'test body'


def test_get():
    """测试是否能正确处理 HTTP和 HTTPS"""
    urls = [
        'http://movie.douban.com/top250',
        'https://movie.douban.com/top250',
    ]
    # 这里就直接调用了 get 如果出错就会直接挂掉，测试得比较简单
    for u in urls:
        get(u)


def test():
    """用于测试的主函数"""
    test_parsed_url()
    test_get()
    test_parsed_response()


if __name__ == '__main__':
    test()
    main()
