def inert_sort(arr):
    
    for i in range(1,len(arr)):
        try:
            for j in range(i-1,-1,-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    print(arr)
                else:
                    break   
        except IndexError:
            pass
    return arr

print(inert_sort([5, 2, 9, 1, 7, 3]))
    
