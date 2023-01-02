# OOP
# Обьектно ориентированное программирование

p = 1


# i = ''
#
# print(type(p))
#
#
# # print(type(i))
# #
# #
# def human(name, age):
#     print(f'my name is {name} age = {age}')
#
#
# human('beka', 19)


# human('nika',11)
# human('adam',8)


class Human:
    brain = True
    heart = True
    # функция = метод
    # конструктор,магический метод
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} is runn')

    def __str__(self):
        return f'{self.name} {self.age} {self.brain}'

    def str(self):
        return f'{self.name} {self.age} {self.brain}'



hum = Human('beka', 19)
# hum.run()
hum2 = Human('adam', 12)



print(hum2.str())
print(hum)


print('e')



# print(hum.name)
# hum.name = 'adam'
# hum.__init__('m',2)
# print(hum.name)
