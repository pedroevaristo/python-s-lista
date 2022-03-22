import math

n = int(input())
t = 0
for b in range(n):
    if(b % 2 == 0):
        t += n
        print(t)