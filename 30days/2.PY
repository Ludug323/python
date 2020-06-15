#Python 運算

#布林值
#== 等於
#!= 不等於 
#> 大於
#< 小於
#>= 大於等於
#<= 小於等於

#布林運算子
#and: 兩者都成立才為true
#or: 其中一個成立就為true
#not: 反向
print('1',True and True)
print('2',True and False)
print('3',True or False)
print('4',False or False)
print('5',not True)
print('6',not False)

print((4>5) or 1==1)
print((4>5) and 1==1) #兩者都要為正確才會是 True

#for 迴圈
for i in range(9,3,-2):
    print(i)

#函式
def my_good_func():
    print("YOU ARE SO GOOD!!")
my_good_func()

import random
random = random.randint(1,10)
print("guess a number between 1 to 10")
while True:
    print("guess!") 
    print("輸入數字 ")
    guess =  int(input())
    if ((guess < 1) or (guess>10)) :
        print("YOU ARE IDIOT!")
    elif guess < random:
        print("too low.")
    elif guess > random:
        print("too high.")
    else:
        print("BINGO!!")
        break