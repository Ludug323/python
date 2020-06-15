while True:
    num = int(input("輸入數字:"))
    count = 0
    for j in range(1,num):
        if num%j ==0:
            count +=1
    if count ==1:
        a = str(num)
        b = int(a[::-1])
        countPir = 0
        for i in range(1,b):
            if b%i == 0:
                countPir += 1
        if countPir ==1 and int(a) != b:
            print(f"{a} is emirp")
        else:
            print(f"{a} is prime")
    else:
        print(f"{num} is not prime")
