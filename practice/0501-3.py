def Fib(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else: 
        return Fib(n-1)+Fib(n-2)
a = int(input("輸入一數字:"))
print(Fib(a))