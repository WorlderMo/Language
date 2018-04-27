import sys

line = int(input())
numList = []
for i in range(line):
    mylist = list(map(int, sys.stdin.readline().split()))
    numList.append(mylist)

#
cyclic = []
numSort = []
for i in range(line):
    oneList = numList[i]
    n = oneList[0]
    for j in range(1, n):
        a = j
        while a < n:
            dif = oneList[a+1]-oneList[j]
            numSort.append(dif)
            a += 1
    numSort.sort()
    cyclic.append(numSort[-1])
for i in cyclic:
    print(i)
