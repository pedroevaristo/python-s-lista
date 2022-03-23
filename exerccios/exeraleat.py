n = int(input())
c = int(input())
t = 1
for b in range(n):
    t *= c
    c = t
print(c)