#import time
#user_input = input()
#print("input text :",user_input)
#print(time.localtime())

#List中的index()方法
list_data = [1,'string',3.1,[5,6,7],[8,9,10]]

print(list_data[4][2])

index = list_data.index('string')#在第幾個索引
print(index)

print(list_data)
list_data.append('good')#append 增加元素

list_data.insert(2,'gogogogog')#insert(索引,元素)插入元素
print(list_data)

list_data.remove(1)#刪除元素
print(list_data)
print("")

mylist2 = ['cat','dog','apple']
mylist2.sort()#整理陣列中的元素
print(mylist2)
print("")

mylist = [1,1,4,5,2,6,7]
mylist.sort()
print(mylist)

print("")

#Python Dictionary字典
my_dic = {
    'name' : 'Jack',"country" : "Taiwan", "Age" : 20
}
print(my_dic['name'])
print(my_dic["country"])
print(my_dic["Age"])
print("")

print(my_dic.keys())
print(my_dic.values())
print("")

#數值轉換
#str()函數

a = 5
a_str = str(a)
print(a_str + " :change number")
print("")
#int()轉換

b = str(3)
print(b)
c = int(b)
print(c)