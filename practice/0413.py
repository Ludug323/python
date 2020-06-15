'''for i in range(8):
    print(" "*(7-i) + "*"*(2*i-1))
for i in reversed(range(7)):
    print(" "*(7-i) + "*"*(2*i-1))'''

num = int(input("輸入一個數字: "))
for i in range(1,num+1):
    c = ""
    a = range(1,i+1)

    for j in range(0,i):
        c += str(a[j])
    if i==1:
        print(" "*(num-i) + c)
    else:
        print(" "*(num-i) + c +c[len(c)-2::-1])