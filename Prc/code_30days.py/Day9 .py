import random
arr = ['asd','axcwq','fofo','gogo']
for i in range(5):
    print(random.uniform(1,2)) #隨機回傳一個浮點數f(1<=f<=2)
print(random.choice(arr))      #隨機回傳arr裡的元素
print("\n\n")

def divMoonCakes(n):
    mooncakes = [n]     #將n轉成list()型態,以便計算
    money = 0
    print(f"月餅小計 {money} 元")
    while mooncakes:        #當mooncakes還有值繼續執行迴圈
        m = random.choice(mooncakes) # m為mooncakes中隨機取得的元素
        mooncakes.remove(m)          #將 mooncakes中的已取得的元素 m 刪除
        print(f"取出 {m} 個月餅")
        div = random.randint(1,m-1)
        print(f"把{m}個月餅分成{div}和{m-div}兩堆，總共增加{div*(m-div)}元")
        money += div*(m-div)
        print(f"目前月餅小計 {money} 元")
        if div != 1:
            mooncakes.append(div)
        if m-div != 1:
            mooncakes.append(m-div)
        if len(mooncakes) >=1:
            print("目前待分月餅堆: ",mooncakes)
    return money
for i in range(10):
    print(f"10個月餅總計{divMoonCakes(10)}元")

def priceOfMooncakes(n):
    return sum(range(1,n))
print(f"10個月餅總計{priceOfMooncakes(10)}元")