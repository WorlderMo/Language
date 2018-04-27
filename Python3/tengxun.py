# coding:utf-8
import sys


class element():
    # 定义机器和任务类
    def __init__(self, time, level):
        self.time = time
        self.level = level

    # x>y calls x.__gt__(y)
    def __gt__(self, other):
        # 运算符重载，方便排序
        if self.time == other.time:
            return self.level > other.level
        return self.time > other.time


def solve():
    # 接收数据
    nm = list(map(int, sys.stdin.readline().split()))
    n, m = nm[0], nm[1]
    # 机器
    machine = []
    for i in range(n):
        time_level = list(map(int, sys.stdin.readline().split()))
        machine.append(element(time_level[0], time_level[1]))
    # 任务
    task = []
    for i in range(m):
        time_level = list(map(int, sys.stdin.readline().split()))
        task.append(element(time_level[0], time_level[1]))
    # 排序
    machine = sorted(machine)
    task = sorted(task)
    # 任务数和收益
    count = 0
    benifit = 0
    # 遍历机器
    for i in range(len(machine)):
        # 选取可完成的最长时间和最高等级任务
        j = 0
        while j < len(task) and machine[i].time >= task[j].time and machine[i].level >= task[j].level:
            j += 1
        # 如果有符合的任务计算收益
        if j > 0:
            count += 1
            j -= 1
            benifit += task[j].time*200 + task[j].level*3
            task.pop(j)
    # 输出结果
    print(count, benifit)


if __name__ == "__main__":
    solve()
