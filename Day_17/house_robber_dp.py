'''Problem Statement: https://leetcode.com/problems/house-robber'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        return self.find(nums,len(nums)-1)
    def find(self, nums,index):
        table=[-1]*(len(nums)+1)
        table[0]=0
        table[1]=nums[0]
        for i in range(1,len(nums)):
            table[i+1]=max(nums[i]+table[i-1],table[i])
        return table[-1]
        
        
