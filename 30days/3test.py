import pandas as pd
print(pd.__version__)
print("")

mydata = [5,2,8,4]
mylist = pd.Series(mydata)
print(mylist)
print("")

mydata1 = pd.Series(mydata,index=['a','b','c','d'])
print(mydata1.index)
print("")

#Dictinary 
mydata2 = {
    'Name' : "王大明",
    'Age'  : "20",
    '喜愛女生年齡' : "7"
}
mydata2 = pd.Series(mydata2)
print(mydata2)

data = {
    'Name' : ["王大明",'阿傑',"小辜","棟棟"],# column : value
    'Age'  : ["20","18","45","32"],
    '喜愛女生年齡' : ["7","18","5","20"]
}
print(data.values())
mydata3 = pd.DataFrame(data)
print(mydata3)
print("")

mydata4 = pd.DataFrame(data,columns=['Name','Age','喜愛女生年齡','地點'])
print(mydata4)
print("")

locate = ['學校','醫院','公司','公園']
locate = pd.Series(locate)
mydata4['地點'] = locate
print(mydata4)