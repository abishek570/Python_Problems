def reverseInGroups(arr, k):
        if k>=len(arr):
            arr2 = []
            for i in range(len(arr)-1,-1,-1):
                arr2.append(arr[i])
            arr = arr2
        else:
            arr2=[]
            for i in range(len(arr)-1):
                if arr[i]==k:
                    for j in range(i,-1,-1):
                        arr2.append(arr[j])
                    arr = arr2
                else:
                    pass
        return arr

arr = [1,2,3,4,5]
k = int(input())
print(reverseInGroups(arr,k))