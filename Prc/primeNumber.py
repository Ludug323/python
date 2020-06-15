def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False  #若有餘數則不是質數(回傳 False),反之.
    return True
    
num = int(input("請輸入一個數字 : "))
numArr = list()
numArr.append(2) #因為從2開始 故它為質數 所以直接進入 numArr裡
checkPrime = False
primeIndex = 0 #check prime index

for i in range(2,num+100): 
    checkPrime = prime(i)
    if checkPrime:#若是質數則加進 numArr裡
            numArr.append(i)
            primeIndex += 1 #質數的index
    if i == num : #若 i 檢查到輸入的值,則輸出 num 前後的質數
        print(numArr[primeIndex-1])
        lenNum = len(numArr) #計算剛好到 num的長度,來判斷後一個的質數
print(numArr[lenNum])