def judge(scores):
    return sorted(scores[1:-1])
#先將列表數字排列(sorted),再來第0個元素跟最後一個元素不取
#切片特性 Arr = [起始位置(包含),結束位置(不包含),步長]
list = [5,2,3,4,3,2,5]
print(judge(list))