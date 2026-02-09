n = int(input("Enter a number to check its a Armstrong Number: "))

n = str(n)

a = []
for i in n:
    i = int(i)
    a.append(i)
length = len(a)

fact = 0
for i in a:
    fact = fact+i**length

if fact == int(n):
    print("It's an Armstrong number")
else:
    print("It's not an Armstrong number")