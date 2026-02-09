## Mean values of a string

def mean(s):
    sums = 0
    for i in s:
        sums+=int(i)
    mean = sums/len(s)
    return mean

print(mean("6666677"))