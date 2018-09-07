
def ToBinary(item):
    while item:
        if item < 1:
            modeValue = item
            break
        else:
            modeValue = item % 2
            yield modeValue
            item = item // 2


def main():
    T = int(input())
    questions = []
    for i in range(T):
        question = list(map(int, input().split()))
        questions.append(question)
    valueSum_max = 0
    guangguns = []
    for question in questions:
        for i in range(question[0], question[1]+1):
            valueSum = 0
            for value in bin(i)[2:]:
                valueSum += int(value)
            if valueSum > valueSum_max:
                valueSum_max = valueSum
                guanggun = i
        guangguns.append(guanggun)
    for i in range(len(guangguns)):
        print("Case {}: {}".format(i+1, guangguns[i]))


if __name__ == '__main__':
    main()
