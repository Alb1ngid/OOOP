# 1 множественное наследование
# MRO method resolution order


class Ded:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def r(self):
        print('спать')


class Father:
    def __init__(self,c):
        self.c=c
    def r(self):
        print('работать')

class Son(Father,Ded):
    def __init__(self, c,a,b):
        Father.__init__(self,c)
        Ded.__init__(self,a,b)

    def r(self):
        print('это метод класса C')
        Ded.r(self)

c=Son('a','a0',2)
c.r()
print(Son.mro())