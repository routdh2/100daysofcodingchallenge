'''Problem Statement: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_1=set(range(1,len(nums)+1))
        set_2=set(nums)
        return list(set_1.difference(set_2))
        
