num = input("輸入數字:")
a = num
x =list()
numRag = 2
for i in range(numRag):
    x.append(a)
    a += num*2
for i in range(numRag):
    x[i] = int(x[i])
print(x)

xSum = sum(x)
print(xSum)

aPrimer = list()
for i in range(1,xSum+1): 
    if xSum %i ==0:
        aPrimer.append(i)
print(aPrimer)