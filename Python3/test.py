# first = input()
# n = int(first.split(" ")[0])  # 课堂持续的时间
# k = int(first.split(" ")[1])  # 保持清醒的时间
# interestMin = [int(i) for i in list(input().split(" "))]
# wakeUp = [int(i) for i in list(input().split(" "))]
# a = len(interestMin)
# t = len(wakeUp)
# localInter = 0
# globalInter = 0
# for i in range(a-k):
#     if wakeUp[i] == 1:
#         globalInter += interestMin[i]
#         localInter += interestMin[i]
#     elif wakeUp[i] == 0:
#         for j in range(k):
#             localInter += wakeUp[i+j]
#             globalInter = max(localInter, globalInter)
# print(globalInter)


# n = int(input())  # 苹果堆数
# num_n = [int(i) for i in list(input().split(" "))]  # 每堆有多少个
# m = int(input())  # 多少次询问了
# num_m = [int(i) for i in list(input().split(" "))]

# sumNum = []
# mysum = 0
# length = len(num_n)
# for i in range(length):
#     mysum += num_n[i]
#     sumNum.append(mysum)
# sumNum_length = len(sumNum)
# for j in num_m:
#     for k in range(sumNum_length):
#         if j <= sumNum[k]:
#             print(k+1)
#             break
