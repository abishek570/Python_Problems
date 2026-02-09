n = int(input("Enter the limit:"))

sums = 0
for i in range(1, n+1):
    sums+=i

print(f"The sum of {n} natural numbers", sums)