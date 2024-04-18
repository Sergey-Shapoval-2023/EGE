import itertools
c = 'ЛЕВИЙ'
a = list(itertools.permutations(c))
k = 0
for i in a:
    i = ''.join(i)
    if i[0]!='Й' and 'ЕИ' not in i:
        k+=1
print(k)


