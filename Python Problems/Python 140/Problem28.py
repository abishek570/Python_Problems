## Factorial Using Recursion

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(5))

## Without loop iteration of pattern

def pattern(N):
        # code here
        m = N
        if N>-5:
            print(N,end=' ')
            pattern(N-5)
            if N>0:
                print(N, end=' ')

def fibonacciNumbers(n):
        # your code here
    arr = []
    a = 0
    b = 1 
    arr.append(0)
    arr.append(1)
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        arr.append(c)
    return arr
            

print(fibonacciNumbers(5))


s = "100100"
a = s.strip("0")
print(a)
