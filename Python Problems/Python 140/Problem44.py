
## Disarium number between 1 to the desired range

def print_disarium(length):
    a = []
    for i in range(1,length):
        sums = 0
        temp = i
        ordi = len(str(i))
        while ordi>0 and temp>0:
            dig = temp%10
            sums+=dig**ordi
            temp//=10
            ordi-=1
        if sums == i:
            a.append(i)
    return a

print(print_disarium(1000))
