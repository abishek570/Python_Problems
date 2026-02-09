fibo = int(input("Enter the number: "))

a = 0 
b = 1
print("-----------Fibonacci Series--------------")
print(a)
print(b)
for i in range(0,fibo):
    c = b+a
    b, a = c, b
    print(c)