"""

Question: Set Mismatch

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

"""

# Using Hashmap -- counter

from collections import Counter

def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    count = Counter(nums)
    # print(count)  --- Counter({2: 2, 1: 1, 4: 1})
    n = len(nums)
    duplicate = -1
    missing = -1
    for i in range(1, n + 1):
        if count[i] == 2:
            duplicate = i
        elif count[i] == 0:
            missing = i
    return [duplicate, missing]

# Test
# print(findErrorNums([1,2,2,4]))
# print(findErrorNums([1,1]))