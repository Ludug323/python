ans = list()

for j in range(100,1000):
    j = str(j)
    for i in range (1,4):
        c = pow(int(j[0]),i)+pow(int(j[1]),i)+pow(int(j[2]),i)
        if c == int(j):
            ans.append(j)
            break
print(ans) 