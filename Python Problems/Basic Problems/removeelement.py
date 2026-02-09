##Leet code - EASY

def remove(nums,val):
    nums = sorted(nums)
    for i in range(0, nums.count(val)+1):
        nums.pop(val)
    return nums 

nums = [1,2,2,2,3,45,6,6,7]
val = 6

print(remove(nums,val))