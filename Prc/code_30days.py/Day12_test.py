def findMin(N,W):
    return min(min(w) for w in W)
example = min([x for x in range(1,10)])
print(example)

a = [[2,5,3,4],[3,5,1,3,4]]
print(findMin(2,a))