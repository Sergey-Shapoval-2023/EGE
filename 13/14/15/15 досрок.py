for a in range(1,1000):
    f = True
    for x in range(1,1000):
        if not ((x % a != 0) <= ((x % 28 == 0) <= (x%49 != 0))):
            f = False
    if f:
        print(a)







