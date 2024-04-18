for num in range(1,100):
    b = bin(num)[2::]

    if num%2==0:
        b+='01'
    else:
        b='1'+ b+'1'
        a = int(b,2)
        if a >156:
            print(a)
