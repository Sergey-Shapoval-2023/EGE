g = 0
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    for f in range(0, 10):
                        if a + b + c == d + e + f:
                            g += 1

print(g)
