
# def multiply()


def main():
    expressionStr = input()
    first_result = []
    result = 1
    # if "/" in expressionStr:
    #     expressionStr.replace('/', '//')
    if ("*" in expressionStr) and ("/" in expressionStr):
        expression = expressionStr.split('*')
        for i in expression:
            if "/" in i:
                item = i.split('/')
                for j in item:
                    first_result.append(eval(j))
                for k in range(len(first_result)):
                    if i == 0:
                        result = first_result[i]
                        continue
                    result = result // first_result[i]
            result *= eval(i)
        print(result)
    elif "*" in expressionStr:
        expression = expressionStr.split('*')
        for item in expression:
            first_result.append(eval(item))
        for num in first_result:
            result *= num
        print(result)
    elif "/" in expressionStr:
        expression = expressionStr.split('/')
        for item in expression:
            first_result.append(eval(item))
        for i in range(len(first_result)):
            if i == 0:
                result = first_result[i]
                continue
            result = result // first_result[i]
        print(result)
    else:
        print(eval(expressionStr))


if __name__ == '__main__':
    main()
