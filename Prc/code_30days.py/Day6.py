# 一.分割.合併
#split分割
S1 = "Horse-Horse-Tiger-Tiger"
print(S1.split("-")) #去除 "-" 符號
                    #['Horse','Horse','Tiger','Tiger']
print(S1.split("Tiger"))#['Horse-Horse-','-','']

S2 = "three    monkey  jumping  on the bed"
print(S2.split()) #默認為空格(多於空格刪除)
print(S2.split(' ')) 
print("------------------------------------")

'''s.join(seq) 以s為分割符,將 seq 中的元素串起來
            成為一個新的字串'''
seq = ["HOW","ARE","YOU"]
print(' '.join(seq))#印出　HOW ARE YOU
print('-'.join(seq))#印出　HOW-ARE-YOU 

L = ["Alice","Bob","Car"]
print("\n".join(L))#\n為換行

# 二.查找
''' s.find(str) 返回str第一次在字串s中出現的index,
                若找不到則返回-1。
    s.count(str) 返回str在字串s中出現的次數'''
s = "believe"
print(s.find("lie"))    #印出  2
print(s.find("le"))     #印出 -1
print(s.count("e"))     #印出  3

#三.替換
#s.replace(str1,str2) 將s中的 str1 替換成 str2
s = "ACCCACAA"
print(s.replace('A','D').lower()) 

'''replace 印出 DCCCDCDD 
    再用lower() 將s字串轉換成小寫'''

for i in range(1,8):
    print(("*"*(2*i-1)).center(13))
