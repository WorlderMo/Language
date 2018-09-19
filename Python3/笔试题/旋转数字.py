# -*- coding: utf-8 -*-
# @Date    : 2018-09-16 19:45:03
# @Author  : mohailang (1198534595@qq.com)


def main():
    N = int(input())
    result = 0
    for i in range(1, N + 1):
        num_str = str(i)
        a = num_str.count('3')
        if num_str.count('3') == 0 and num_str.count('4') == 0 and num_str.count('7') == 0:
            if ('5' in num_str) or ('2' in num_str) or ('6' in num_str) or ('9' in num_str):
                result += 1
    print(result)


if __name__ == '__main__':
    main()
