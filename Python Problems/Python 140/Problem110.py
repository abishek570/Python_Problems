## Indices of capital letters

def index_of_caps(s1):
    a = []
    for i in range(len(s1)):
        if s1[i].isupper():
            a.append(i)
    return a

print(index_of_caps("eDaBiT"))


## Even numbers list using list comprehension

n = int(input("Input Range: "))

a = [i for i in range(1,n+1) if i%2==0]

print(a)