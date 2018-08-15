# -*- coding: utf-8 -*-
# @Date    : 2018-08-15 14:59:00
# @Author  : mohailang (1198534595@qq.com)

import socket

# 创建 socket 对象
s = socket.socket()  # http
# s=ssl.wrap_socket(socket.socket())    # https

host = 'g.cn'
port = 80

# 连接主机
s.connect((host, port))


# 得到本机 ip和端口
ip, port = s.getsockname()
print('ip and port {} {}'.format(ip, port))

# 构造一个 http请求
http_request = 'GET / HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)
# 发送请求
request = http_request.encode('utf-8')
print('请求', request)
s.send(request)  # 只接受 bytes类型数据

# 接受服务器的响应数据
response = s.recv(1023)
print('响应数据', response.decode('utf-8'))
