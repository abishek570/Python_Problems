## Binary Search Algorithm

import random

a = [random.randint(1,1000) for i in range(10)]

a = sorted(a)

print(a)

def bin_search(arr, target):
    l = 0
    h = len(arr)-1
    for i in range(len(arr)):
        mid = (l+h)//2
        if arr.count(target)>1:
            for j in range(len(arr)):
                if arr[j] == target:
                    return j 
        if target == arr[mid]:
            return f"{target} is in the {mid}th index" 
        elif target > arr[mid]:
            l = mid+1
        elif target < arr[mid]:
            h = mid-1
    else:
        return "Element not found"

for i in a:
    print(bin_search(a,i))

b = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
print(bin_search(b, 3))
