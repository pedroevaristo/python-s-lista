import math
#from xml.etree.ElementTree import C14NWriterTarget
lista = []

for y in range(5):
    c=int(input())
    lista.append(c)

g=0
while g < 5:
    lista.sort(reverse = True)
    g+=1

print(f'O maior numero: {lista[0]}')
