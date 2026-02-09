## Element index +++

def element_index(lis1):
    for i in range(len(lis1)):
        lis1[i] = lis1[i] + i
    return lis1

print(element_index([5,4,3,2,1]))