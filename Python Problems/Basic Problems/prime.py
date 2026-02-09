for n in range(100000):
    if n == 1:
        print(f"{n} --> Composite")
    elif n<0:
        print(f"{n} --> Negative numbers")
    elif n == 0:
        print(f"{n} --> Zero")
    else:
        for i in range(2,n):
            if (n%i==0):
                a = f"{n} -->  is not a prime"
                break
        else:
            a = f"{n} --> Prime"
        print(a)

