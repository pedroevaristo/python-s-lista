# Agora é Switch-Case. A questão pede com base a ordenação de vetores.Muito dificil.
#pula esta questão:
import math
num=[]#Aqui vai estar armazenado os valores digitados
print('Digite 3 números:')

for k in range(3):
    k=int(input())
    num.append(k)
#print(num)

print('\n---------\n')

x=int(input('Escolha um de 1 a 3:'))

if x == 1:
    num.sort()
    print(num)

if x == 2:
    num.sort(reverse=True)
    print(num)

if x == 3:
    num.sort(reverse=True)
    if num[0] > num[1]:
        print(num[0])
