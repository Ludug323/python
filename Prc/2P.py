#質數
# sum = 0
# a = 0
# arr = list()
# for i in range(1,20):
#     if i%2!=0:
#         sum= i
#         arr.append(i)
#         print("質數為:{:2} , a:{:2}".format(i,a))
#         a += 1
def x (*num):
    for i in num:
        print("1~",inp,"中的偶數為: ",i)
arr = list()
inp = int(input("請輸入要計算的最大範圍: "))
for i in range(1,inp+1):
    if i %2==0:
        arr.append(i)
x(arr)