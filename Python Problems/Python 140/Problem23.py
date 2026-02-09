## Greatest Common Divisor

n1 = int(input())
n2 = int(input())

if n1>n2:
    smaller = n2
elif n1<n2:
    smaller = n1

for i in range(smaller+1,0,-1):
    if (n1%i==0) and (n2%i==0):
        hcf = i
        break
print(hcf)

