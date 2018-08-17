# -*- coding: utf-8 -*-
# @Date    : 2018-08-15 18:56:39
# @Author  : mohailang (1198534595@qq.com)

import socket

# 服务端的 host为空，表示接受任意 IP 地址的请求
host = ''
port = 20000

s = socket.socket()
# bind 用于绑定主机和端口
s.bind((host, port))


# 处理请求
while True:
    # 监听
    s.listen(5)

    # 当有客户端过来接连的时候，会返回两个值，分别是连接和客户端 IP 地址
    connection, address = s.accept()

    # 接受数据
    request = connection.recv(1024)

    print('ip and request {}\n{}'.format(address, request.decode('utf-8')))

    response = b'<h1>hello mohailang!</h1>'

    # 用 sendall发送给客户端
    connection.sendall(response)

    connection.close()
