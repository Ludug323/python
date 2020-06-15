class practice:
    a = 1
    def check(self):
        return print(self)
x = 1
print(practice.a)
practice.check("hihi")

class complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
    
x = complex(3.0,4.5)
print(x.r,x.i)