class E:

    def __init__(self, name):
        self.name = name


class D:

    def __init__(self, age):
        self.age = age


class C:

    def method_c(self):
        print('это метод класса С')


class B:

    def method_b(self):
        print('это метод класса B')


class A(B, C, D, E):

    def __init__(self, name, age):
        E.__init__(self, name)
        D.__init__(self, age)


a = A('Ali', 19)
a.method_b()
a.method_c()
print(a.name, a.age)
print(A.mro())
