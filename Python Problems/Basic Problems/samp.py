def avg(n,*args):
    a = [n]
    a.append(*args)
    return sum(a)/len(a)

print(avg(2,5))