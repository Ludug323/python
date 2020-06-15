'''
def hanoi(n,a,b,c):
    if n ==1:
        print(f"將1號金片從{a}移到{c}石柱")
    else:
        hanoi(n-1,a,c,b)
        print(f"將{n}號金片從{a}移到{c}石柱")
        hanoi(n-1,b,a,c)
hanoi(4,'A','B','C')

def stair(n):
    return stair(n-1)+stair(n-2) if n>=2 else 1
print(stair(3))

def fx(n):
    print(f"進入第{n}層")
    if n ==3:
        return 0
    fx(n+1)
    print(f"退出第{n}層")
fx(1)
'''

def fc(num):
    if num==1:
        return print(a*num)
    fc(num-1)
    print(a*(num))
    
n = 9
a = n    
fc(n)