a = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]

def search(arr,tar):
    l = 0
    r = len(a)-1
    m = (l+r)//2
    while l<=r:
        if a[m]==tar:
            if a[m]==a[m-1]:
                pass
            else:
                return m
        elif a[m]>tar:
            l = 0
            r = m-1
            m = (l+r)//2
            if arr[r]==tar:
                return r
        elif a[m]<tar:
            l = m+1
            r = len(a)-1
            m = (l+r)//2
            if arr[l]==tar:
                return l
        if tar not in a:
            return -1 

print(search(a,3))