num = tuple(range(0,10))
print(num)

a = [x for x in num if x%3 ==0]
a.pop(0)
count =0
for i in a:
    print(i)
    count +=1
print(f"3的倍數:{count}")

icy1 = ['a','b','c','d']
icy2 = 50
icy3 = [1,2,3]
icy4 = (3,6)
icy5 = [3,2,1,4,5]

print(icy1)
icy1.insert(1,icy2)
print(icy1)
icy1.insert(3,icy3)
print(icy1)
icy1.insert(0,icy4)
print(icy1)

print(sorted(icy5))

icy = ['a','b','c','d','a','a','c']
count = icy.count(icy[0])
print(f"a : {count}")

x = icy.copy()

print(x)
print(True if x is icy else False)#判斷x 跟 icy 是否為同個記憶體位址

#------集合(Set)------
a = {1,2,3,4,5,6}
b = {1,3,5,7,9,11}

print(f"a: {a}")
print(f"b: {b}")

c = a.difference(b) #做差集運算 = a-b
print(c) #{2,4,6}
c = a.union(b)      #做聯集運算 = a|b
print(c) #{1,2,3,4,5,6,7,9,11}

#frozenset()
a = frozenset({1,2,3,4,5,6})
print(type(a))
print(a)


#字典(Dictionary)
a = {
    1 : 'a',
    2 : 'b',
    3 : 'c',
    4 : 'd'
}

print(a,type(a))

a = dict(zip((1,2,3,4),('a','b','c','d')))
print(a,type(a))
#   遞迴函數(重要!!)
'''
def fact(n):
    return 1 if n == 1 else n*fact(n-1)
n = 5
num = fact(n)
print(num)'''


'''
def hanoi(n,a,b,c): #將石柱a的n個圓盤移到石柱c(b為輔助)
    if n==1:
        print(f"將1號金片由{a}石柱移動到{c}石柱")
    else:
        hanoi(n-1,a,c,b)
        print(f"將{n}號金片由{a}石柱移動到{c}石柱")
        hanoi(n-1,b,a,c)
        
hanoi(4,'A','B','C')'''