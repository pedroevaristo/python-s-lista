import math
x=int(input('Digite o lado: '))
y=int(input('Digite o lado: '))
z=int(input('Digite a base: '))

t=int

if x == z and z==y:
    print('Equilatéro', x, z, y)

elif x == y:
    print('Isóceles', x, y, z)

elif x != z and y != x:
    print('Scaleno', x, y, z)