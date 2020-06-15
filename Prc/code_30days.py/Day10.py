def reverseStr(s):
    return s[::-1]
print(reverseStr("desserts"))    # stressed
print(reverseStr("牙刷"))        # 刷牙

def pefectShuffle(deck):
    n = len(deck)//2
    first = deck[:n]    #取出前n個數字當做第一副牌
    second = deck[n:]   #取出後n個數字當作第二副牌
    nextIsFirst = True  #紀錄下一張要發的牌是第一副牌還是第二副牌
    firstIdx = 0        #紀錄下一張要發的牌的index
    secondIdx = 0       #紀錄下一張要發的牌的index
    for i in range(n*2):
        if nextIsFirst:
            deck[i] = first[firstIdx]
            firstIdx += 1
        else:
            deck[i] = second[secondIdx]
            secondIdx +=1
        nextIsFirst = not nextIsFirst
    return deck

def pefectShuffleSed(deck):
    n = len(deck)//2
    deck[::2],deck[1::2] = deck[:n],deck[n:]
    return deck
str = list(range(1,11)) #[1,2,3,4,5,6,7,8,9,10]
print(pefectShuffle(str))

str = list(range(1,11))
print(pefectShuffleSed(str))

A = [0] *30
A[::3] = [1] *len(A[::3])
A[::5] = [1] *len(A[::5])
print(sum(A))