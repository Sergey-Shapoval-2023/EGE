ip = '113.191.169.34'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
ip = '113.191.160.0'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))