# -*- coding: utf-8 -*-
# @Date    : 2018-09-15 10:48:47
# @Author  : mohailang (1198534595@qq.com)


def main():
    string = input()
    words = []
    if ',' in string:
        str_list = string.split(',')
        for item in str_list:

            sub_list = item.split()
            for j in sub_list:
                words += [j]
            words += ','
        words.pop()
    else:
        words_list = string.split()
        for item in words_list:
            words += [item]
    result = ''
    length = 0
    for word in words:
        if word not in result or word == ',':
            result += word
            result += ' '

    for i in words:
        if i != ',' and i != ' ':
            length += 1

    print('The number of words in this passage is:{},{}'.format(length, result))


if __name__ == '__main__':
    main()
