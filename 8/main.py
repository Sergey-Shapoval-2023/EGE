from itertools import product

# Из числа в строку
# print(list(product('ЛРНТ', repeat=5))[149])

# Из строки в число
'''
count = 0
for line in product('АОУ', repeat=5):
    if ''.join(line) == 'УАУАУ':
        print(count + 1)
        break
    count += 1
'''

import itertools
# itertools - библиотека для работы с комбинаторикой
# product() - функция, получающая все возможные перестановки элементов длины repeat из букв, которые в неё переданы
list_values = itertools.product('БОРИС', repeat=6)
count = 0
for str in list_values:
    # join() - функция соединяющая массив строк в одну строку при помощи разделителя, который указан до точки
    line = ''.join(str)
    # count() - строковая функция, которая определяет кол-во вхождений букв или слов в строку
    if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') < 2:
        count += 1
print(count)