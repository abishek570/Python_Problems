def sortArr(arr): 
        #code here
    print(arr)
    for i in range(len(arr)-1):
        if i == 0:
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            print("Now", arr)
        if i>0:    
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                print("arr1",arr)
                if arr[i]<arr[i-1]:
                    temp = arr[i-1]
                    arr[i-1] = arr[i]
                    arr[i]=temp
                    print("arr2",arr)
    return arr

print(sortArr(arr=[8,1,5,3,2,4,7]))