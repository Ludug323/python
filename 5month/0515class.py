class Test:
    sal = 0
    cnt = 0
    def __init__(self, name, tel, sal):
        self.name = name
        self.tel = tel

        Test.sal += sal
        Test.cnt += 1

    def un(self):
        print(self.name)
    def pn(self):
        print(self.tel)

    @classmethod
    def count_ppl(cs):
        return cs.cnt
    @classmethod
    def count_avg(cs):
        return (cs.sal / cs.cnt)    

x = Test('Abc','11111',50000)
y = Test('errr','22222',35000)

a = Test.count_avg()
b = Test.count_ppl()
print(a)
print(b)