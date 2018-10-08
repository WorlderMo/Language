# -*- coding: utf-8 -*-
# @Date    : 2018-09-21 19:35:29
# @Author  : mohailang (1198534595@qq.com)


def main():
    water = []
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        if len(a) == 1 or len(a) == 0:
            water.append(0)
        else:
            water.append(result(a))
    for i in water:
        print(i)


def result(a):
    # print("a:", a)
    if len(a) == 0:
        # print("empty")
        return 0
    if len(a) == 1:
        # print(a)
        return 0
    mid = a.index(max(a))
    left = a[:mid]
    right = a[mid+1:]
    # print("left:", left)
    # print("right:", right)
    v_left = 0
    v_right = 0
    if left:
        left_max_index = left.index(max(left))  # 0
        v_left = max(left) * (mid - left_max_index)  # 4 * (2-0)
        # print("v_left:", v_left)
        v_left += result(left[:left_max_index+1])
    if right:
        right_max_index = right.index(max(right))  # 0
        v_right = max(right) * (right_max_index + 1)  # 3 * (0+1)
        # print("v_right:", v_right)
        v_right += result(right[right_max_index:])
    # print(v_left, v_right)
    return v_left + v_right

    # left[:left_max_index + 1]  # []
    # right[right_max_index:]  # [3,2]
    # return v_left + v_right + result(left[:left_max_index+1]) + result(right[right_max_index:])


if __name__ == '__main__':
    main()
