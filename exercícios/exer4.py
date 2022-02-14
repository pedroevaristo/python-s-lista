x = int(input('digite um num. par: '))
y = int(input('digite um num. impar: '))

if x % 2 == 0 :
    print('Este numero', x, 'eh par')
elif x % 2 != 0:
    print('Numero nao eh par!')
if y % 2 == 1 :
    print('Este numero', y, 'eh impar')
elif y % 2 != 1:
    print('Numero nao eh impar!')
