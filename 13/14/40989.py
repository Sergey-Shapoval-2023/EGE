x = 2 * 216**8 + 4 * 36**12 + 6**15 - 1296
count = 0
while x > 0:
    if x%6 ==0:
        count+=1

    x//=6

print(count)


