## Formula based Problem

D = str(input("Comma seperated input: "))

C = 50
H = 30

a = D.split(",")

print(a)
import math

for i in range(len(a)):
    D = int(a[i])
    a[i] = int(math.sqrt((2*C*D)/H))
    a[i] = str(a[i])

s = ""
for i in range(len(a)):
    s = s+a[i]
    if i<len(a)-1:
        s+=","

print(s)