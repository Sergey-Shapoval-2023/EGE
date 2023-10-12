for num in range(2, 1000):
    b = bin(num)[2:]
    b += b[1] + b[0]
    if int(b, 2) > 74:
        print(num)
        break
