import math

d = int(input())

g=0;

for f in range(1, d+1):
    if d % f == 0:
        print('\033[32m', end='')
        g+=1
    else:
        print('\033[31m', end='')

    print('{} '.format(f), end='')
if g ==2:
    print(f'\nNumero primo é: {d}')