import itertools
a = itertools.product('ЗИМА', repeat = 5)
count = 0
for str in a:
    b = ''.join(str)
    if (b.count('И') == 1 and not 'А' in b) or (b.count('А') == 1 and not 'И' in b):

        print(b)
        count+=1
print(count)
