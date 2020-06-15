#break 的簡易範例
# n = 0
# while n<5:
#     if n==3:
#          break
#     print(n)
#     n += 1 
# print("最後的 n:",n)

#  contiune 的簡單範例
# n = 0
# for x in [0,1,2,3]:
#     if x%2==0: # x是偶數
#         continue
#     print(x) #0,1,3
#     n += 1
# print("最後的 n:",n) #n = 2

#else 的簡易範例
# sum = 0
# for n in range(10):
#     sum += n
# else:
#     print(sum)# 印出 0+1+2...+10的結果

#綜合範例: 找出整數平方根
#輸入 9.得到3
#輸入 11.得到[沒有]整數的平方根

n = input("輸入一個正整數:")
n = int(n)
for i in range(n):# i 從 0~n-1
    if i*i == n:
        print("整數平方根",i)
        break# 用  break 強制結束迴圈時，不會執行else區塊
print("沒有整數平方根")
# x = 1
# while x:
#     n = int(input("輸入一個正整數"))
#     if n**0.5%1==0:
#         print("正數平方根",n**0.5)
#     else:
#         print("沒有整數平方根")
#         break