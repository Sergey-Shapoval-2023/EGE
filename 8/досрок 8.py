import itertools
b = itertools.product('АПРСУ', repeat = 5)
i = 1

for str in b:
    line = ''.join(str)

    if line.count('У')<=1 and 'АА' not in line:
        break
    i+=1


print(i)









