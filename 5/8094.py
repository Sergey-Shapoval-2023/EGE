a = 50
b = bin(a)[2::]
sumd = 0
for i in b:
    sumd+=int(i)
b = b+str(sumd%2)
sumd = 0
for i in b:
    sumd += int(i)
b = b + str(sumd % 2)
print(b)
