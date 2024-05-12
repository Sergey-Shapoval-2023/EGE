import itertools
a = itertools.product('КОНФЕТА',repeat = 5)
count = 0
for str in a:
    b = ''.join(str)
    if b.count('Е') == 2 and b[1] != 'Ф':
        count+=1

print(count)
