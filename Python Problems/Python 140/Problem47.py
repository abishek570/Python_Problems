
n = int(input())
a = []
for i in range(1,n):
    b = i*(i+1)
    if b<=n:
        a.append(b)
    else:
        break

print(a)
