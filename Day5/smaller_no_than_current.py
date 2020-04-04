#Problem Statement: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                    count+=1
            result.append(count)
        return result
