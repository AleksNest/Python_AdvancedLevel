import sys

from decimal import Decimal
import math
import decimal

'''
1 Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
'''

x1 = 5
x2 = 5.3
x3 = "строка"
x4 = True
x5 = None
x6 = []
x7 = {}
x8 = set()
x9 = frozenset()
print(x1, x2, x3, x4, x5, x6, x7, x8, x9)
print(f' тип переменной {x1} - {type(x1)}')
print(f' тип переменной {x2} - {type(x2)}')
print(f' тип переменной {x3} - {type(x3)}')
print(f' тип переменной {x4} - {type(x4)}')
print(f' тип переменной {x5} - {type(x5)}')
print(f' тип переменной {x6} - {type(x6)}')
print(f' тип переменной {x7} - {type(x7)}')
print(f' тип переменной {x8} - {type(x8)}')
print(f' тип переменной {x9} - {type(x9)}')
