def duplicates(arr):
    arr = sorted(arr)
    arr2=[]
    arr3=[]
    for i in arr:
        if i not in arr2:
            arr2.append(i)
        elif i in arr2:
            if i in arr3:
                pass
            else:
                arr3.append(i)
    return arr3

print(duplicates(arr=[2,2,2,2,3,3,3,3,4,4,5,2,1]))