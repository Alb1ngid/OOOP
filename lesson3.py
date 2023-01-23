# полиморфизм наследование
# инкапсуляция
# 1 - открытый  2 - защищенный 3 - скрытый
class Student:
    time = True

    def __init__(self, mark, id):
        self.id = id
        self.mark = mark


s1 = Student(10, 12)


class Human(Student):
    def __init__(self, mark, id, timesleep, name):
        super().__init__(mark, id)
        self.__times = timesleep
        self._name = name

    time = False

    def __str__(self):
        return f'{self.id} {self.mark} {self.time} {self._name}'

    def _stop(self):
        print('stop')

    def __none(self):
        print('extra stop')


s2 = Human(10, 1, False, 'Данияр')
print(s2)

s2.id = 32
s2._name = 'name'
print(s2._name)
print(s2)

s2.__time = 1
s2._stop()
print(dir(Human))

s2._Human__none()
print(s2._Human__times)


class Obj:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __run(self):
        print(f'{self.__name} running')

    def run(self):
        self.__run()

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, a):
        self.__name = a

    def get_obj(self):
        return f'{self.__name}'
    def set_obj(self, a):
        self.__name = a


s11 = Obj('Бе ктур', 18)
s11.name = 'Бектур'
print(s11.name)

s11.set_obj('Бектур')
print(s11.get_obj())