class Calculator:

    def __add__(self, other):
        if isinstance(other, self.__class__):
            self._balance = self._balance + other._balance
        if isinstance(other, (int, float)):
            self._balance = self._balance + other

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            self._balance = self._balance * other._balance
        if isinstance(other, (int, float)):
            self._balance = self._balance * other

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            self._balance = self._balance - other._balance
        if isinstance(other, (int, float)):
            self._balance = self._balance - other

    def __rsub__(self, other):
        return self - other

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            self._balance = self._balance / other._balance
        if isinstance(other, (int, float)):
            self._balance = self._balance / other

    def __rtruediv__(self, other):
        return self / other
