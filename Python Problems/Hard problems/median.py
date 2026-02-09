## Leet code -- HARD

# def median(nums,nums2):
l =[1,2,3]
l2=[4,5,6]
l3 = l+l2
if len(l3)%2!=0:
    print(l3[len(l3)//2])
elif len(l3)%2==0:
    a = l3[len(l3)//2] + l3[(len(l3)//2)-1]
    print(a/2)