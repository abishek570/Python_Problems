## Sum of cube of the natural numbers

n = int(input("Enter the range: "))

cube = 0

a = []

for i in range(1,n+1):
    cube+=i**3
    a.append(cube)
print(a)
print(cube)