# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

multipliers = []
divisor = 2

n = int(input('Введите число: '))

while n != 1:
    if n % divisor == 0:
        n /= divisor
        multipliers.append(divisor)
    else:
        divisor += 1

print(multipliers)
