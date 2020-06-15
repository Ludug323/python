num = int(input("輸入一數字:"))
a = list(range(1,num+1))
b = 0
while len(a) != 1:
    for i in range(0,3):
        if i==2:
            a.pop(b)
            b -=1#長度減一則b也須減一
        if b == (len(a)-1):#若數到跟a相同大小時,則重新記數
            b = 0
        else:    
            b +=1            
print(a)