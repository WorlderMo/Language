# -*- coding: utf-8 -*-
# @Date    : 2018-09-16 19:23:32
# @Author  : mohailang (1198534595@qq.com)


def main():
    g = list(map(int, input().split()))
    s = list(map(int, input().split()))
    result = 0
    g.sort()
    s.sort()
    index_s = 0
    index_g = 0
    # for i in range(len(s)):
    #     for j in range(i, len(g)):
    #         if s[i] >= g[j]:
    #             result += 1
    #             break
    while index_s < len(s) and index_g < len(g):
        if s[index_s] >= g[index_g]:
            result += 1
            index_g += 1
        index_s += 1
    print(result)


if __name__ == '__main__':
    main()
