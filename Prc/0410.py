n = int(input())
a = 1
count = 0
for i in range(1,n+1):
    a  = i*a
'''while(1):
    if a%10==0 :
        count += 1
        a = a//10
    else :
        break'''
while a%10==0: #while 布林值:
               #直接看a!總積除於10 餘數是否為0
    count += 1 #若尾數為0 則count +1
    a = a//10  #並且將a整除於10
print(count)