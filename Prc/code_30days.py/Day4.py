sorces = [60,20,70,40,80]
print(sum(sorces)/len(sorces))

print(pow(3,2))#3的2次方

print(abs(-9))#-9的絕對值

print(max([(1,0),(1,1),(2,1),(2,0)]))

import time 

tStrat = time.time()#計時開始
print(pow(1234,456789,10))
tEnd = time.time()#計時結束
print("Total time = %f seconds"%(tEnd - tStrat))