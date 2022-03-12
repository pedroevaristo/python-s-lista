import math

a  = int(input())
print('(-)')
b  = int(input())
print('______')

t = b

for h in range(1,a+1):
    
    t-= a
    print(abs(t))
    if t == 0:
        break
