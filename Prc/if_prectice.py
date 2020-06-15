sorce = int(input("請輸入你的國文成績 : "))
result = "pass" if sorce > 60  else  "Fail" #if變化敘述 
print("測試結果 : {}".format(result))
if sorce > 60 :
    print("你的成績是{}分".format(sorce))
    print("恭喜你喔")