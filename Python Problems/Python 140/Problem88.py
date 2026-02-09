## Even number Generator

n = int(input("enter the number range: "))

def generate_even(n):
    for i in range(n):
        if i%2 == 0:
            yield i

a = generate_even(n)
b = ",".join(map(str,a))

print(b)