x = 25**5 + 5**14 - 5
count = 0
while x > 0:
    if x%5==4:
        count+=1
    x = x//5
print(count)
