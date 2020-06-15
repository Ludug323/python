num = int(input("輸入一個數字:"))
numBack = num

#flag
#往前數哪個數字為質數
count = 0
while(1):
    num += 1
    #num%2 , num%3 , num%4 , num%5......,num%11
    for i in range(2,int((num**0.5)+1)):
        if num%i==0:
            count += 1
    if count ==0:
        break
    else:
        count = 0
print(num)

#flag
count = 0
while(1):
    numBack -=1
    for i in range(2,int((numBack**0.5)+1)):
        if numBack%i==0:
            count += 1
    if count ==0:
        break
    else:
        count = 0
print(numBack)