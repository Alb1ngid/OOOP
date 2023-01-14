from calculator import Calculator


class Bank(Calculator):
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self, plus_balance):
        self._balance = plus_balance + self._balance
        return f'Вы внесли {plus_balance}, теперь баланс вашего счёта составляет {self._balance}'

    def _kill(self, minus_balance):
        self._balance = self._balance - minus_balance
        return f'Вы сняли {minus_balance}, теперь баланс вашего счёта составляет {self._balance}'

    def __jackpot(self):
        self._balance = self._balance * 10
        return f'Поздравляем! Вы сорвали джекпот, теперь баланс вашего счёта состввляет {self._balance}'

    def _copy_balance(self, copy):
        self._balance = copy._balance + self._balance
        return f'Вы скопировали баланс у {copy._name} теперь баланс вашего счёта составляет: {self._balance}'


a = int(input('Введите сумму которую хотите добавить на свой счёт: '))
b = int(input('Введите сумму которую хотите снять с вашего счёта: '))
test = Bank('Max', 5)
# print(test._name)
# print(test.moneyX(a))
# print(test._kill(b))
# print(test._Bank__jackpot())
test2 = Bank('Vika', 10)
# print(test._copy_balance(test2))
# print(Calculator.__add__(test, test))
print(test._balance)
test * test2
print(test._balance)
