s = "0025"
print(int(s))   #轉換成整數
print(float(s)) #轉換成浮點數
print(list(s))  #轉換成列表
print(tuple(s)) #轉換成元組
print(set(s))   #轉換成集合 

L = [1,2,3]
M = (1,2,3)
L[0] = 2  # L會變成[2,2,3]
#M[0] = 2  # 這一行會出現TypeError

a = "hello "
a += "world"
print(a)
#列表版本 - 冰箱
fridge = ['香蕉','蘋果','香蕉']
b = fridge
b += ['臭掉的牛奶']
print(fridge) #['香蕉','蘋果','香蕉','臭掉的牛奶']

#字串版本 - 冰箱
fridge =  '蛋糕, 蘋果, 香蕉'
b  = fridge
b += ', 臭掉的牛奶'
print(fridge) # '蛋糕, 蘋果, 香蕉'

def reverseNum(n):
    sign = '-' if n<0 else ''
    return int(sign + str(abs(n))[::-1])
print(reverseNum(123))
print(reverseNum(2300))
print(reverseNum(-250))
print(reverseNum(0))