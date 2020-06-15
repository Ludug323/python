'''num = int(input("輸入數字:"))

flag = True
while flag:
    print(f"num is {num} >10")
    newNum = int(input("輸入數字:"))
    if(newNum <10):
        flag = False
else:    
    print("NOT IN")'''

#序對(Tuple)
icy = ("abc", 123, 'A', 'I', "30", "Python", 1.3)
#Index   0     1    2    3     4       5      6  

print(icy[:])

print(icy[3])

print(icy[5])

print(len(icy))
print("")

for i in icy:
    print(i)

icy2 = (("Curry",30,"GWS") , ("LBJ",23,"CLE"))
for i in icy2:
    print(i)
    print("")

for i, c ,y in icy2:
    print(i)
    print(c)
    print(y)
    print("")

icy = ("abc", 123, 'A', 'I', "30", "Python", 1.3)
icy2 = (("Curry",30,"GWS") , ("LBJ",23,"CLE"))
icy3 = ('a','b','c','d','c','b','a')

print(icy.index("Python"))

print(icy2.index(("Curry",30,"GWS")))

print(icy3.count('a'))#計算'a'在icy3有幾個
print("")

tupleA = (range(10))
count = 0#記數3有幾個
Alist = list()
for i in tupleA:
    i +=1
    if i%3 == 0:
        count += 1
        Alist.append(i)
print(f"3的倍數為{Alist}")
print(count)