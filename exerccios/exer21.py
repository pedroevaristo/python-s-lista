import math
from re import T

n = int(input())
t = 1
f = n
while f > 0 :
    print('\n{}'.format(t))
    t *= f#Era simplesmente fazer -1 no numero digitado.
    f-=1    

print('\n',t)
#for f in range(n, 1, -1)