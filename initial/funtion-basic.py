#定義函式
#函式內部的程式碼,若是沒有函式呼叫,就不會執行
# def multiply(n1,n2):
#     return n1*n2

#呼叫函式
# value = multiply(3,4)+multiply(10,5)#(3*4)+(10*5)
# print(value)

# 程式的包裝
def calculate(num):
    sum = 0
    for n in range(1,num+1):
        sum = sum+n
    return sum

n = int(input("輸入1到多少的加法 "))
print("1+...+",n,"的結果為:",calculate(n))