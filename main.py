# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target
# nums = [2,7,11,15], target = 9

def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(1 + i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return None

print(two_sum([2,7,11,15], 9))

"""1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9"""

a = 1
for i in range(1, 12):
    if i % 2 != 0:
        print(str(i) * a)
        a = a + 1

