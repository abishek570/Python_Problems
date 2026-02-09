## Least Common multiplier

num1 = int(input())
num2 = int(input())

if num1>num2:
    greater = num1
else:
    greater = num2

while(True):
    if (greater%num1==0) and (greater%num2==0):
        lcm = greater
        break
    else:
        greater+=1
print(lcm)

print(ord('z'))