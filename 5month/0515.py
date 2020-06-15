def f(s,offset):
    if offset == 0:
        return s
    for _ in range(len(s)-(offset%len(s))):
        s.append(s.pop(0))
        print(s)
    return s
s = ['a','b','c','d','e','f','g']
print(f(s,3))