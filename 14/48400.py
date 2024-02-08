for x in '0123456789A':
    res = int(f'95{x}2', 11) + int(f'{x}458', 12)
    if res % 136 == 0:
        print(res // 136)
        break
