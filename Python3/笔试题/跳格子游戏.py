# -*- coding: utf-8 -*-
# @Date    : 2018-09-16 19:36:44
# @Author  : mohailang (1198534595@qq.com)


def main():
    n = int(input())
    if n <= 1:
        print(1)
    else:
        state = [1, 1]
        for i in range(n - 1):
            a = state[-1] + state[-2]
            state.append(a)
        print(state[-1])


if __name__ == '__main__':
    main()
