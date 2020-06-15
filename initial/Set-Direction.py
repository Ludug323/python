# 集合的運算
# s1 = {3,4,5}
# print(10 not in  s1)
# print(3 in s1)
# s1 = {3,4,5}
# s2 = {4,5,6,7}
# s3 = s1&s2  #交集:取兩個集合中,相同的資料{4,5}
# s3 = s1|s2 #聯集:取兩個集合中的所有資料，但不重複取{3,4,5,6,7}
# s3 = s1-s2 #差集:從S1中,減去和S2重疊的部分{3}
# s3 = s1^s2 #反交集:取兩個集合中,不重疊的部分{3,6,7}
# str = set("Hello")# set(字串)
# print(str)
# print(s3)

# 字典的運算 : key-value 配對
dic1 = {"apple":"蘋果","bug":"蟲蟲"}
print(dic1["apple"])

dic2 = {"apple":"蘋果","bee":"蜜蜂","car":"車","bug":"蟲蟲"}
# del dic["apple"] #刪除字典中的鏈值對(kry-value pair)
# print(dic)

# dic = {x:x*2 for x in [3,4,5]}
# print(dic)