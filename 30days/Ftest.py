import pandas as pd

df = pd.read_csv(r'C:\Users\loge7\OneDrive\桌面\AniGamerInfo-master\DailyData\AGI_Daily_20190413-0100.csv')
print(df.tail())

data = {'name': ['Bob', 'Nancy','Amy','Elsa','Jack'],
        'year': [1996, 1997, 1997, 1996, 1997],
        'day':[11,23,8,3,11],
        'month': [8, 8, 7, 1, 12]
        }

mydata = pd.Series(data,index = ["q","w","e","r"])
print(mydata)

mydata1 = pd.DataFrame(data,columns=["name","year","day",'month','number'])
print(mydata1)
number = [1,2,3,4,5]
mydata1["number"] = number

print(mydata1)
y = len(mydata1['name'])