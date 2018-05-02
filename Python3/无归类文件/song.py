# coding: utf-8
import sys


def cal_combination(x, n):
    result = 1
    for i in range(x + 1 - n, x + 1):
        result *= i
    return result


def solve():
    k = int(sys.stdin.readline().strip())
    axby = list(map(int, sys.stdin.readline().split()))
    a, x, b, y = axby[0], axby[1], axby[2], axby[3]
    result = 0
    if a < b:
        a, b = b, a
        x, y = y, x
    m = k // a
    for i in range(1, m + 1):
        temp = (k - (i * a)) // b
        if (i * a + temp * b) == k:
            result += cal_combination(x, i) * cal_combination(y, temp)
    return result % 1000000007
if __name__ == '__main__':
    print(solve())
