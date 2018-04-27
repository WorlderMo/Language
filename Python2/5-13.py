# conding: utf-8

def sumMin(time):
    HH, MM = time.split(":")
    summin = int(HH) * 60 + int(MM)
    return summin

if __name__ == '__main__':
    print "time format as HH:MM : "
    time =raw_input("> ")
    print sumMin(time)
