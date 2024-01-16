for x in range(61,100):
    s = x*"1"
    while '111' in s:
        s = s.replace('111','2',1)
        s =s.replace('222','11',1)
        if s == '221':
            print(x)
