import calculator
class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self, plus_balance=int(input('Введите сумму которую хотите добавить на свой счёт: '))):
        self._balance = plus_balance + self._balance
        return f'Вы внесли {plus_balance}, теперь баланс вашего счёта составляет {self._balance}'

    def _kill(self, minus_balace=int((input('Введите сумму которую хотите снять с вашего счёта: ')))):
        self._balance = self._balance - minus_balace
        return f'Вы сняли {minus_balace}, теперь баланс вашего счёта составляет {self._balance}'

    def __jackpot(self):
        self._balance = self._balance * 10
        return f'Поздравляем! Вы сорвали джекпот, теперь баланс вашего счёта состввляет {self._balance}'

    def _copy_balance(self, copy):
        self._balance = copy._balance + self._balance
        return f'Вы скопировали баланс у {copy._name} теперь баланс вашего счёта составляет: {self._balance}'


test = Bank('Max', 100)
print(test._name)
print(test.moneyX())
print(test._kill())
print(test._Bank__jackpot())
test2 = Bank('Vika', 200)
print(test2._copy_balance(test))

