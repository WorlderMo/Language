import sys
# 计算排列组合


def cal_combination(x, n):
    result = 1
    for i in range(1, n+1):
        result *= (x+1-i)
        result /= i
    return int(result)


def solve8():
    # 接收数据
    k = int(sys.stdin.readline().strip())
    axby = list(map(int, sys.stdin.readline().split()))
    a, x, b, y = axby[0], axby[1], axby[2], axby[3]
    result = 0
    if a < b:
        a, b = b, a
        x, y = y, x
    m = k//a
    for i in range(1, m+1):
        # 判断能否整除
        temp = (k-(i*a))//b
        if (i*a+temp*b) == k:
            # 能整除排列组合计算种数
            result += cal_combination(x, i) * cal_combination(y, temp)

    return result % 1000000007
