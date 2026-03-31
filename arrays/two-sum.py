#Problem: Two Sum
#Link: https://leetcode.com/problems/two-sum/
# Approach: HashMap — store complement, O(n) time, O(n) space


def twoSum (nums , target):
    seen = {}
    for i , num in enumerate(nums):
        complemnet = target - num 
        if complemnet in seen :
            return [seen[complemnet] , i]
        seen [num] =  i

