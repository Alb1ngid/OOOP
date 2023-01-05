class Human:
    head = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}'

    def run(self):
        print(f'{self.name} running')


pu = Human('Эркинбеков Бекзат', 14)
pu1 = Human('Торобаев Баймурат', 14)
# print(pu)
# pu.run()
# pu1.run()
# Human.run(pu)
# print(pu.age)



class Func:
    def x2(self,q):
        print(self,q * 2)

# Func.x2(pu.name,pu.age)


# наследование полиморфизм инкапсуляция

class Student(Human):
    def __init__(self, name, age,id,group):
        # super().__init__(name, age)
        Human.__init__(self,name,age)
        self.id=id
        self.group=group

    def fly(self):
        print(f'{self.name} is fly')

    def run(self):
        print(f'теперь {self.name} бегает очень быстро')

    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}\n' \
               f'id is {self.id}\n' \
               f'group is {self.group}'


s=Student('Евтушенко Максим',27,1,'26-3')
# s.run()
# print(s)
# s.fly()
print(s)

# q1w2eedxfv