import itertools
a = itertools.product('ПЯТНИЦА', repeat = 5)
count = 0
for str in a:

    b = ''.join(str)
    if b[0] != 'Н' and b.count('Я') == 1:
        count +=1
print(count)






