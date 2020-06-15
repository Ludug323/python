import pandas as pd
print(pd.__version__)

#資料類型 - Series

my_obj = pd.Series([4,7,-5,3])
print(my_obj.values)

print(my_obj.index)
print("")
my_obj2 = pd.Series([8,9,10,11], index=['a','b','c','d'])
print(my_obj2)
print(my_obj2.index)
print("")

print("a" in my_obj2)#查詢是否存在my_obj2

#Dictinary轉成Series

dic_obj3 = {'name' : 'apple','birthday' : '1999-03-23','LuckyNumber' : '36'}
my_obj3 = pd.Series(dic_obj3)
print(my_obj3)
print("")

#Series內部資料型態
registration = [True,False,True,False]
registration = pd.Series(registration)
print(registration)

#資料類型 - DataFrame
data = {'name': ['Bob', 'Nancy','Amy','Elsa','Jack'],
        'year': [1996, 1997, 1997, 1996, 1997],
        'day':[11,23,8,3,11],
        'month': [8, 8, 7, 1, 12]
        }
myframe = pd.DataFrame(data)
print(myframe)
print(myframe['name'][1])
print("")

myframe2 = pd.DataFrame(data,columns=['name','year','month','day'])
print(myframe2)
print("")
myframe3 = pd.DataFrame(data,columns=['name','year','month','day','LuckyNum'])
print(myframe3)

LuckyNum = ['3','2','1','7','3']
LuckyNum = pd.Series(LuckyNum)
myframe3['LuckyNum'] = LuckyNum
print(myframe3)