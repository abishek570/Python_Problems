def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]: 
                arr[j],arr[j+1] = arr[j+1],arr[j]
            else:
                pass    
        print(f"{i}th iteration = {arr}")
    return arr
b = bubble_sort([64, 34, 25, 12, 22, 11, 90])
print(b)

a = [0, 1, 2, 0, 1, 2]
print(sorted(a))

