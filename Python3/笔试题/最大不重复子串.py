# -*- coding: utf-8 -*-
# @Date    : 2018-09-09 10:01:43
# @Author  : mohailang (1198534595@qq.com)


def main():
    string = input()
    if len(string) == 0 or string is None:
        print(0)
    else:
        location = ''
        result = ''
        for item in string:
            if item not in location:
                location += item
            elif item in location:
                index = location.find(item)
                location = location[index+1:]
            if len(location) > len(result):
                result = location
        print(len(result))


if __name__ == '__main__':
    main()
