# -*- coding: utf-8 -*-
# @Date    : 2018-09-15 17:31:27
# @Author  : mohailang (1198534595@qq.com)


def main():
    array = eval(input()[1:-1])
    result = []
    n = int(input())
    if n == 0:
        for item in array:
            if ',' in item:
                item = item.strip('[').strip(']')
                temp = item.split(',')
                for i in temp:
                    result.append(int(i))
            else:
                result.append(int(item))
        print(result)
    if n != 0:
        for item in array:
            if '[' in str(item):
                item = str(item)
                for i in range(n):
                    if '[' in item:
                        item = item[1:-1]
                result.append(eval(item))
            else:
                result.append(item)
        print(result)


if __name__ == '__main__':
    main()
