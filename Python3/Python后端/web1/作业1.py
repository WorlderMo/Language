# -*- coding: utf-8 -*-
# @Date    : 2018-08-15 22:42:57
# @Author  : mohailang (1198534595@qq.com)

import socket
import ssl


def parsed_url(url):
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u = url

    if '/' in u:
        host = u.split('/')[0]
        path = u.split('/')[1]
    else:
        host = u

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
    return socket


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


def main():
    print(parsed_url('http://hailng:321/ssss'))


if __name__ == '__main__':
    main()
