# -*- coding: utf-8 -*-
# @Date    : 2018-09-26 19:56:31
# @Author  : mohailang (1198534595@qq.com)


class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    decode = {}

    def __init__(self, weight):
        self.node = [Node(kid[0], kid[1]) for kid in weight]
        while len(self.node) > 1:
            self.node.sort(key=lambda x: x.value, reverse=True)
            kid_node = Node(value=(self.node[-1].value + self.node[-2].value))
            kid_node.left = self.node.pop(-1)
            kid_node.right = self.node.pop(-1)
            self.node.append(kid_node)
        self.root = self.node[0]
        self.list = list(range(100))

    def build(self, tree, length):
        node = tree
        string_decode = ''
        if not node:
            return
        elif node.name:
            for i in range(length):
                string_decode += str(self.list[i])
            self.decode[node.name] = string_decode
            return
        self.list[length] = 0
        self.build(node.left, length + 1)
        self.list[length] = 1
        self.build(node.right, length + 1)

    def get_decode(self):
        self.build(self.root, 0)
        return self.decode


def machine():
    password = input()
    letter_set = set(password)
    str_dict = {}
    char_weights = []
    result = ''
    for i in letter_set:
        str_dict[i] = password.count(i)
    for key in str_dict:
        char_weights.append((key, str_dict[key]))
    tree = Tree(char_weights)
    decode_dict = tree.get_decode()
    for i in password:
        result += decode_dict[i]
    print(result)


if __name__ == '__main__':
    machine()
