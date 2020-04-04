#Problem Statement: https://leetcode.com/problems/create-target-array-in-the-given-order
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        for i,index_pos in enumerate(index):
            target.insert(index_pos,nums[i])
        return target
        
