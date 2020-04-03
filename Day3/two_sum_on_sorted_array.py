#Problem Statement: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while left<right:
            sum=numbers[left]+numbers[right]
            if target==sum:
                return [left+1,right+1]
            elif target>sum:
                left+=1
            else:
                right-=1
