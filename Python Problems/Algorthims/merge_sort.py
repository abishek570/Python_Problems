def merge(a,b):
    c = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
            print(f"Print1:-{c}")
        else:
            c.append(b[j])
            j+=1
            print(f"Print2:-{c}")
    while i<len(a):
        c.append(a[i])
        i+=1
        print(f"Print3:-{c}")
    while j<len(b):
        c.append(b[j])
        j+=1
        print(f"Print4:-{c}")
    return c

def merge_sort(arr):
    if len(arr)==1:
        return arr
    else:
        print("The array", arr[:len(arr)//2])
        print("The array", arr[len(arr)//2:])
        return merge(merge_sort(arr[:(len(arr)//2)]),merge_sort(arr[(len(arr)//2):]))

arr = merge_sort([5,1,3,2,4])

print(arr)