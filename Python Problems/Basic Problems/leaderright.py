arr = list(input())

def leaders(arr):
        res=[]
        res.append(arr[-1])
        m=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>=m:
                res.append(arr[i])
                m=arr[i]
        res1=[]
        for i in range(len(res)-1,-1,-1):
            res1.append(res[i])
        return res1

print(leaders(arr))