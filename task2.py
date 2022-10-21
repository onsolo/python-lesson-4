# Задача 2. В первой строке файла находится информация об ассортименте мороженного,
# во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

with open('icecream.txt', encoding='UTF-8') as data:
    text = data.readlines()

assortment = text[0].split(', ')
storage = set(text[1].split(', '))

assortment = set(map(lambda item: item.rstrip('\n'), assortment))

diff = ''.join(assortment.difference(storage))
print(f'Мороженое {diff} закончилось ((')

