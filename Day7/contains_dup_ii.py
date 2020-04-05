'''Problem Statement: https://leetcode.com/problems/contains-duplicate-ii/'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for index,value in enumerate(nums):
            dic[value]=dic.get(value,[])+[index]
        for value in dic.values():
            if len(value)>1:
                for i in range(0,len(value)-1):
                    if abs(value[i]-value[i+1])<=k:
                        return True
        return False
        
