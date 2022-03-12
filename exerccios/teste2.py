#fazer denovo este exercicio.

for j in range(50):
    if j > 1:
        for k in range(2, j):
            if(j % k==0):
                break
        else:
            print(j)
