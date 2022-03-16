#from tkinter import Listbox
n = int(input())
lis = []
t = 0
for s in range(n):
    if s > 1:
        for h in range(2,s):
            if(s % h ==0):
                break
        else:
            s+=2
            t+=s
            lis.append(t)

print(lis)