import threading

def myrun(low, high):
    for i in range(low,high) :
        print(i, end = ' ',flush = True)
        if i % 100 == 0 :
            print()
            


def myrun2(low, high):
    for i in range(low,high) :
        print(chr(i), end = ' ',flush = True)
        if i % 100 == 0 :
            print()
t = threading.Thread(target=myrun, args=(1,100000))
t.start()


t2 = threading.Thread(target=myrun2, args=(1,100000))
t2.start()