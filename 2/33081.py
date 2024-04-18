s = '>'+ '1'*25+'2'*17+'3'*10
while ('>1' in s) or ('>2' in s) or ('>3' in s):
    if '>1' in s:
        s = s.replace('>1','22>3',1)
    if '>2' in s:
         s = s.replace('>2','2>',1)
    if '>3' in s:
        s = s.replace('>3','11>2',1)


print(s)
n = 0
for i in s[0:-1]:

    n+=int(i)
print(n)









