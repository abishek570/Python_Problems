n = str(input("Enter the number for testing:"))

a = str(n)

import re

b = re.findall('[1-9]',a)
print(b)
j = 0
for i in b:
    a = int(i)
    j+=(a**len(b))

if  j == n:
    print(f"{j} is an Armstrong Number")
else:
    print(f"{n} is not an armstrong number")

