#有序可變動列表 List

grades = [12,60,15,70,90]
print("原本 : ",grades,"數字\n") 
print("更改地一個數字為 55\n")
grades[0] = 55
print("更改過後 : ",grades,"\n")

length = len(grades)
print("List 的長度 :",length,"\n")

#grades = grades + [12,30]
#print("增加新的成績 : ",grades,"\n")

#grades[1:4]=[]#刪除1~3的資料不包含第四的資料
#print("刪除1~3的成績: ",grades,"\n")

       #第0區間  #第1區間
data = [[3,4,5] , [6,7,8]]
print("第[1][1]的資料 :",data[1][1],"\n")

data[0][0:2] = [5,5,5]
print("變動資料[0][0:2] :",data,"\n")

#Tuple 有順序不可更動資料
data = (3,4,5)
print("資料[0:2] : ",data[0:2],"\n")
#data[0] = 5 #沒辦法更動資料
#print(data[0])