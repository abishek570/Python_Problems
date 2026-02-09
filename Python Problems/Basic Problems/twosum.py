def two_sum(arr, tar):
    arr = sorted(arr)
    l = 0
    h = len(arr)-1
    for i in range(len(arr)):
        if arr[l]+arr[h]==tar:
            return (arr[l],arr[h])
        elif arr[l]+arr[h]>tar:
            h-=1
        elif arr[l]+arr[h]<tar:
            l+=1
    else:
        return False

print(two_sum([1,2,4,3,6,10],tar = 11))

for i in range(1,11):
    print(f"78 x {i} = {i*78}")