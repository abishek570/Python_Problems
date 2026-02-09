def prepare(arr,low,high):
    pivot = arr[high]
    item = low-1
    for i in range(low, high):
        if arr[i]<=pivot:
            item+=1
            print("Items:-", item)
            arr[item], arr[i] = arr[i], arr[item]
            print("Modified Array:- ",arr)
    arr[item+1], arr[high] = arr[high], arr[item+1]
    print("Modified array 2:- ",arr)
    return item+1


def quick_sort(arr, low, high):
    if low<high:
        pivot = prepare(arr, low, high)
        print("Pivot:- ",pivot)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)
    
arr= [3,1,5,9,7]
quick_sort(arr, low=0, high=len(arr)-1 )
    
print(arr)