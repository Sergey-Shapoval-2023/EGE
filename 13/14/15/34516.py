for a in range(64):
    f = True
    for x in range(64):
        if not((x & 28 != 0) or (x & 45 != 0)) <= ((x & 48 == 0) <= (x & a != 0)):
            f = False
    if f:
        print(a)
        break
