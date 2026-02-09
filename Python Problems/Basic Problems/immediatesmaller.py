arr = [4, 2, 1, 5, 3]

def immediateSmaller(arr):
    # Fix indentation here
    a = []
    for i in range(0, len(arr) - 1):  # Correct indentation
        if arr[i] > arr[i + 1]:
            a.append(arr[i + 1])
        else:
            a.append(-1)  # This covers both cases (arr[i] < arr[i+1] and arr[i] == arr[i+1])
    
    a.append(-1)  # Append -1 for the last element as it has no next element
    return a  # Correct indentation

arr2 = str(arr)
print(arr2)
arr3 = arr2.strip('[]')
