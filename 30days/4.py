x = [2,4,5,6,1,3,5,10,3]
y = len(x)

print(y)
for i in range (y-1):#8
    for j in range(y-i-1):
        if(x[j]<x[j+1]):
            x[j],x[j+1] = x[j+1],x[j]
print(x)
