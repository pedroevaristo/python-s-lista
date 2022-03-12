import math
def maiorNumeroEPrimos():
    numeros = []
    for i in range(1, 11):
        valor = int(input('Digite o ' + str(i) + '° número: '))
        numeros.append(valor)
    print(max(numeros), 'é o maior número da lista.')
    for i in numeros: 
        if i>1: 
            for j in range(2,i): 
                if(i % j==0):
                    break
            else: 
                print(i, 'é um número primo.') 

maiorNumeroEPrimos()

#_______________
def maiorNumeroEPrimos(numeros):
    print(max(numeros), 'é o maior número da lista.')
    for i in numeros: 
        if i>1: 
            for j in range(2,i): 
                if(i % j==0): 
                    break
            else: 
                print(i, 'é um número primo.') 
    
    
maiorNumeroEPrimos(range(0,10))