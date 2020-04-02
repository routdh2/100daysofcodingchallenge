#Problem Statement: https://leetcode.com/problems/remove-element/
'''Submission Detail: 113 / 113 test cases passed.
Runtime: 32 ms
Memory Usage: 13.9 MB'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start=0
        for index,value in enumerate(nums):
            if value==val:
                pass
            else:
                nums[start]=value
                start+=1
        return start
