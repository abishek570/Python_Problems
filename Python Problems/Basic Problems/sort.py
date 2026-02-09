## Sorting binary array

def binSort(arr):
        # code here
    for i in range(len(arr)):
        if arr[i]==0:
            arr[0]=0
        elif arr[i]==1:
            arr[-1]=1
    return arr

arr = [1,0,1,1,0,1,1,1,0,0,0]
print(binSort(arr))