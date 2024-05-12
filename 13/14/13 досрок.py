count = 0
for x in '01':
    for y in '01':
        for z in '01':
            for w in '01':
                for e in '01':
                    s = x+y+z+w+e
                    if (13 + s.count('1'))%4==0:
                        count+=1
print(count)




