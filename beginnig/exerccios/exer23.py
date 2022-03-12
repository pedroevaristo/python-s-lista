n = int(input())
list = []

for f in range(1,n):
    if n % f == 0:
        print('{}'.format(f))
        list.append(f)

list.sort(reverse=True)
print(list[0:3])
    
    