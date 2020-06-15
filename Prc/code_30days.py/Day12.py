scores = [20,30,50,60,25,70]
adject = 100 - max(scores)
newScores = [x+adject for x in scores]
print(sorted(newScores))

# 生成1~10的平方數
powNew = [pow(x,2) for x in range(1,11)]
print(powNew)

# 將字串轉為字元陣列
s = "Hello"
sList = [x for x in s] #亦可直接寫list(s)
print(sList)

# 雙for迴圈生成全排列
Str = [m + n for m in 'abc' for n in '123']
print(Str)

def sumOfDigit(num):
    return sum([int(c) for c in str(num)])

print(sumOfDigit(120))
for j in range(1,10):
   print(" ".join([f"{j}*{i}={j*i:2d} " for i in range(1,10)]))