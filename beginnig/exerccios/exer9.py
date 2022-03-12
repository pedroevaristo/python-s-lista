import math
x=int(input('Digite seu ano de nascismento para ver se tem idade para votar: '))

t = int

t = 2022 - x
if t >= 18:
    print('Sua idade', t, '. Pode tirar a carteira de mostorista.')

elif t <= 16:
    print('É de menor, só pode votar.')