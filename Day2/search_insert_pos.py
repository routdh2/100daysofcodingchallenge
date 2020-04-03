#Problem Statement: https://leetcode.com/problems/search-insert-position/
'''Submission Detail: 62 / 62 test cases passed.
Runtime: 44 ms
Memory Usage: 14.5 MB'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            index=nums.index(target)
            if index!=-1:
                return index
        except ValueError as e:
            if target<nums[0]:
                return 0
            elif target>nums[-1]:
                return len(nums)
            else:
                for i,value in enumerate(nums):
                    if target>value and target<nums[i+1]:
                        return i+1
