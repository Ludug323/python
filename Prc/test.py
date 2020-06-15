#while True:
#    try :
#        n = input()
#        print("hello, " + n)
#    except:
#        break
while True:
    try:
        x = [int(x) for x in input().split()]
        y = len(x)
        if y < 3 :
            continue
        if x[1]/x[0] == x[2]/x[1]:
            a = (x[3]//x[2])*x[3]
            x.append(a)
            print(x[0],x[1],x[2],x[3],x[4])
        else :
            a = x[3] +1
            x.append(a)
            print(x[0],x[1],x[2],x[3],x[4])
    except:
        break