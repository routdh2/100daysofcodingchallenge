#Problem Statement: https://leetcode.com/problems/two-sum/
'''Submission Details: 29 / 29 test cases passed.
Runtime: 52 ms
Memory Usage: 14.9 MB'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}
        for i in range(len(nums)):
            key=target-nums[i]
            if key in dictionary:
                return [dictionary[key],i]
            else:
                dictionary.update({nums[i]:i})
