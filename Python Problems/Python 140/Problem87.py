## Divisible by 7 and 5 Generators

n = int(input("Enter a range of number: "))

def generate_5_or_7(n):
    for i in range(0,n):
        if (i%5==0) and (i%7==0):
            yield i

a = generate_5_or_7(n)

for i in a:
    print(i)