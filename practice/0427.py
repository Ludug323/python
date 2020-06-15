'''
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

def minNum(x,y):
    n = x*y
    return n//gcd(x,y)

x = int(input("輸入數字:"))
y = int(input("輸入數字:"))
print(f"x: {x}, y: {y}")

maxfactor = gcd(x,y)
num = minNum(x,y)
print(f"最大公因數:　{maxfactor}")
print(f"最小公倍數:　{num}")
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n== 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
nlist = [0,1]
for i in range(1,n+1):
    n3 = nlist[i-1] + nlist[i]
    nlist.append(n3)

for i in range(0,n+1):
    print(nlist[i])

print(fibonacci(n))