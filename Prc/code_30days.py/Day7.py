def isEven(n):
    return n%2 == 0 #此為條件判斷式
print(isEven(5))

n = 5
T = "n是整數" if n%2 == 0 else "n不是整數"
print(T)

word  = "apple"
if word[0] in 'aeiou': # in也可當條件判斷 
    print("單字開頭為母音")
print("a" in word) # A in B 判斷A是否在B容器中

def sumOfList(nums):
    return sum(nums) if len(nums) !=0 else -1

def sumOfList_1(nums):
    return nums and sum(nums) or -1
print(sumOfList([1,2,3]))
print(sumOfList_1([1,2]))