
import lesson4
import math
print(math.pi)

from math import pi as e
print(e)

# 2 собвственные модули
import lesson4

a=lesson4.Son('a','a',12)
a.r()

from lesson4 import Father
f=Father('отец')
f.r()

from lesson4 import colorama
# 3 внешние
import fastapi
import colorama

print(colorama.Back.RED)
