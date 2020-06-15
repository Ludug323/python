'''Python 精簡語法之一 : 切片
newArr = L[起始位置(包含) : 結束位置(不包含) : 步長]'''

foodArr=["香雞堡", "豬肉堡", "牛肉堡",
 "總匯三明治", "鮪魚三明治", "火腿三明治"]

print(foodArr[1:3])#第二個參數不包含foodArr[3]的元素
#如果第一個參數是0,可以省略
foods = foodArr[:3]
print(foods)

#若第二個參數省略,表示從起始位置直接起取道列表結束
# Example :
foods = foodArr[3:]
print(foods)

#若同時省略
fridge = ["蛋糕","蘋果","香蕉"]
b = fridge[:]
b.remove("蛋糕")
print("列表b的內容為 : {}".format(b))   
print("列表fridge的內容為 : {}".format(fridge))

#Python 持以負數索引取值
print(foodArr[-1])#foodArr[-n]　便是取得列表的倒數第n個元素

print(foodArr[-2:])#切片一樣支援負數索引

#加入步長參數

print("奇數項元素 : {}".format(foodArr[::2]))
print("偶數項元素 : {}".format(foodArr[1::2]))

#　字串切片
numStr = "123456789"
print(numStr[-4:])

print(numStr[7:4:-1])

#   range函數
#range(起始位置（包含),結束位置(不包含),步長)
print(range(5))

#若要印出數字
#方法一
for i in range(5):
    print(i)
#方法二
print(list(range(5)))
print(list(range(2,6)))
print(list(range(4,21,3)))

holidays = list(range(1,31))

for i in range(2,31,3):
    holidays[i] = "姐姐放假"

for i in range(4,31,5):
    holidays[i] = "妹妹放假"

for i in range(14,31,15):
    holidays[i] = "姐妹都放假"
print(holidays)#印出結果