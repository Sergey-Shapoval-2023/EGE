for x in '0123456':
    for y in '0123456':
        res = int(f'{y}{x}320',7) + int(f'1{x}3{y}3',9)
        if res % 181 == 0:
            print(res // 181)
            break

