a = str(input())
def reverse(a):
    b = []
    for i in range(len(a)-1,-1,-1):
        b.append(a[i])
    for j in b:
        print(j,end='')

reverse(a)