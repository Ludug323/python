class x:
    def __init__(self):
        self.x = 0
        self.y = 0

    def g(self,num,cou):
        self.x = num
        self.y = cou
        

a = x()
a.g(1,1)
print(a.x)