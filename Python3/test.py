def transfer(string):
    result = ''
    tran = False
    for i in range(len(string)):
        if tran == True:
            result += string[i].upper()
            tran = False
            continue
        if string[i] == '_':
            tran = True
            continue
        result += string[i]
    return result


if __name__ == '__main__':
    print(transfer('this_is_a_test'))
