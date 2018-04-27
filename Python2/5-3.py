def socre(num):
    if num>=90 and num <=100:
        return 'A'
    elif num >=80:
        return 'B'
    elif num >=70:
        return 'C'
    elif num >= 60:
        return 'D'
    else:
        return 'F'  

if __name__=='__main__':
    n = input()
    print socre(n)
