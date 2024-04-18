for A in range(64):
    f = True
    for x in range(64):
        for y in range(64):
            if not ((2*x + 3*y < 30 ) or (x + y >=A)):
                f = False
    if f:
        print(A)

