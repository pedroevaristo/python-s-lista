import math
x=float(input('Digite a nota 1: '))
y=float(input('Digite a nota 2: '))
z=float(input('Digite a nota 3: '))
t = float

t=((x+y+z)/3)

print(t)

if t > 6.0:
    print('Aprovado!')
elif t >= 4.9 or t <= 5.0:
    print('Recuperação!')
else:
    print('Reprovado!')