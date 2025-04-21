
from math import sqrt, floor
import math

num = int(input('digite um numero: '))
raiz = math.sqrt(num)
raiz = sqrt(num)

print('A raiz de {} e igual a {:.2f}'.format(num, math.ceil(raiz)))
print('A raiz de {} e igual a {:.2f}'.format(num, math.floor(raiz)))
print('A raiz de {} e igual a {:.2f}'.format(num, (raiz)))


"""
import random
num = random.randint(1, 10)
print(num)
"""

"""
import emoji
print(emoji.emojize("Olá, mundo :globe_showing_Americas:"))
"""