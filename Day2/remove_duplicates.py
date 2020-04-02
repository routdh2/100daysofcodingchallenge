#Problem Statement: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''Submission Detail: 161 / 161 test cases passed.
Runtime: 80 ms
Memory Usage: 15.5 MB'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set=set()
        start=0
        for index,value in enumerate(nums):
            if value not in nums_set:
                nums_set.add(value)
                nums[start]=value
                start+=1
            else:
                pass
        return start
