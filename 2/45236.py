print("z,w,x,y")
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                f = not (x <= w) or (y == z) or y
                if not f:
                    print(z,w,x,y)

