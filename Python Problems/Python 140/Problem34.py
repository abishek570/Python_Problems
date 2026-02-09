## Array Rotation

arr =list(input())
r = int(input())

if r<0 or r>len(arr):
    print("Invalid Rotation Factor")
else:
    arr[:] = arr[r:]+arr[:r]
    for i in arr:
        print(i,end='')
