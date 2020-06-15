#---------Time 函數-------
'''
import time
timeTick = time.time() #從1970,1-1,0:00:00 到現在 的秒數
print(timeTick)

gmtime = time.gmtime()
localtime = time.localtime()#台北標準時間
gmtimeTest = time.gmtime(123.45)
print(gmtime)
print(gmtimeTest)
print(localtime)

asctime = time.asctime()
print(f"asctime : {asctime}")

ctime = time.ctime()#預設為目前時區的時間
ctimeTest = time.ctime(112231)
print(ctime)
print(ctimeTest)
strftime = time.strftime("%Y/%m/%d",time.localtime())#將時間函數格式化輸出
print(strftime)
strftimeTest = time.strftime("%Y/%m/%d, %p. %H:%M:%S, %A",time.localtime())
print(strftimeTest)
'''

'''
#--------Function 函數---------
#EX 1:
def area(r):
    return r*r*3.14

r = 6.7
print(f"半徑: {r} ,面積: {area(r)}")

#EX 3:
def sum(n):
    x = 0
    for i in range(1,n+1):
        x += i
    return x
num = int(input("輸入數字: "))
print(f"輸出1+2+...+{num} = {sum(num)}")

for j in range(1,10):
    print(" ".join([f"{j}*{i}={j*i:2d} " for i in range(1,10)]))

#EX4:
def bmiFun(c,k):
    m = c/100
    bmi = k/(m*2)
    if bmi<18:
        print("過輕")
    elif bmi<24:
        print("正常")
    elif bmi<27:
        print("稍重")
    else:
        print("肥胖")
cm = int(input("身高:"))
kg = int(input("體重:"))
bmiFun(cm,kg)
'''

'''
def multi_para(r):
    x = r*r*3.14
    y = r*r
    z = r*r*r
    return x,y,z
r = 5
ans = multi_para(r)
a,b,c = multi_para(r)
print(a,b,c)

icy = lambda i,j : i**j
print(icy(5,3))

def fact(n):
    if n ==1:
        return 1
    else:
        return n*fact(n-1)
n = 5
print(fact(n))
'''

def flag(n):
    if(n[::-1]==n[::]):
        return "是"
    else:
        return "不是"

num = input("輸入一數字>=10:")
numlist =list()
for i in num:
    numlist.append(i)
ans  = flag(num)
print(ans)