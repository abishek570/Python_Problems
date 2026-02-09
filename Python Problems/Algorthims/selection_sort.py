def select_sort(arr):
    cur_idx = 0
    min_index = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
            else:
                pass
            
        arr[cur_idx],arr[min_index] = arr[min_index],arr[cur_idx]
        print(f"{i} iteration:- {arr}")
        cur_idx+=1
        min_index=cur_idx
    return f"Sorted Arrray:- {arr}" 

# a = select_sort([91, 14, 73, 27, 85, 6, 42, 3, 59, 98, 17, 5, 77, 21, 80, 49, 63, 11, 94, 35, 2, 68, 8, 52, 9, 70, 24, 46, 19, 89, 30, 55, 12, 76, 4, 61, 28, 95, 15, 82, 37, 7, 50, 90, 23, 66, 10, 43, 32, 57, 1, 79, 26, 87, 40, 92, 18, 65, 29, 54, 16, 72, 38, 84, 5, 47, 20, 69, 33, 97, 13, 75, 22, 86, 41, 60, 31, 99, 17, 56, 25, 81, 39, 62, 45, 78, 34, 96, 12, 51, 74, 27, 83, 44, 67, 23, 58, 11, 71, 36, 93, 48, 88, 53, 10, 64, 26, 79, 37, 9, 42])
b = select_sort([5,1,2,3,4])

# print(a)
print(b)
