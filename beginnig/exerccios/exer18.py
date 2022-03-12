import math

lista = []

for j in range(5):
    x = int(input())
    lista.append(x)

k=0;
while k < 5:
    lista.sort(reverse = True)
    k+=1

print(f'{lista[0]} ')
#____________________________
k=0;
for v in range(5):
    if v % lista == 0:
        k+=1

    if k == 2:
        print('Número primo: {} \n'.format(v))