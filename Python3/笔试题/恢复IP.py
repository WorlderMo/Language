# -*- coding: utf-8 -*-
# @Date    : 2018-09-09 10:55:03
# @Author  : mohailang (1198534595@qq.com)


def dfsHelper(string):
    ips = []
    return dfs(string, 0, ips, '')


def dfs(string, sub, ips, ip):
    if sub == 4:
        if string == '':
            ips.append(ip[1:])
            return
    for i in range(1, 4):
        if i <= len(string):
            if int(string[:i]) <= 255:
                dfs(string[i:], sub + 1, ips, ip + '.' + string[:i])
                if string[0] == '0':
                    break
    return ips


if __name__ == '__main__':
    string = input()
    ips = dfsHelper(string)
    print(len(ips))
