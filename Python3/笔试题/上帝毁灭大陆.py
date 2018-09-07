def main():
    nums = list(map(int, input().split()))
    height, width, waterLevel = nums[0], nums[1], nums[2]
    area = 0
    level = []
    for i in range(height):
        a = list(map(int, input().split()))
        level.append(a)
    for item in level:
        for i in item:
            if i > waterLevel:
                area += 1
    print(area)


if __name__ == '__main__':
    main()
