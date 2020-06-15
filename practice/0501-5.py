fullBat = int(input("輸入一數字:"))
recoverBat = 0
emptyBat = 0
c = 3-fullBat%3    
if fullBat %3 !=0:
    recoverBat = (fullBat+c)//3 #16//3 =5
    emptyBat = fullBat%3 #16%3 = 1
else:
    recoverBat = fullBat//3 #16//3 =5
    emptyBat = fullBat%3 #16%3 = 1

b = recoverBat + emptyBat
a = 0
if b >=3:
    a = b//3
total = fullBat + recoverBat  +a
print(total)

