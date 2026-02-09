## TCS Problem

n = int(input("Enter a number: "))

a = []
for i in range(2,n):  
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        a.append(i)
print(f"List of Prime numbers between 2 to {n}: ",a)

sum = 0
for i in range(len(a)):
    sum+=a[i]
print(f"Sum of Prime numbers between 2 to {n}: ",sum)