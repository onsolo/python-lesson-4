# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа.
# 3 -> 3.142
# 5 -> 3.14159

import math

accuracy = int(input('Введите точность числа пи: '))
print(round(math.pi, accuracy))
