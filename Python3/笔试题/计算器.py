# 假设有这样一个计算器，该计算器只有两个按钮，按下第一个按钮能使显示数值减少1，按下第二个按钮能使显示数值乘以2，当前显示数值为N，那么至少要按多少次按钮才能使显示数值变成M？
def main():
    nums = list(map(int, input().split()))
    N, M = nums[0], nums[1]
    num = 0
    while True:
        a = abs(N - 1 - 5)
        b = abs(N * 2 - 5)
        if a > b:
            N *= 2
            num += 1
        else:
            N -= 1
            num += 1
        if N == M:
            break
    print(num)


if __name__ == '__main__':
    main()
