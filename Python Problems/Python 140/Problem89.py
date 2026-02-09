a = int(input("Enter the range of fibanocci series: "))

def fibo_comprehension(a):
    if a == 0:
        return 0
    elif a == 1:
        a = [0,1]
        b = ",".join(map(str,a))
        return b
    elif a>1:
        seq = [0,1]
        [seq.append(seq[-1]+seq[-2]) for i in range(2,a)]
        return ",".join(map(str,seq))
print(fibo_comprehension(a))