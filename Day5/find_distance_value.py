#Problem Statement: https://leetcode.com/problems/find-the-distance-value-between-two-arrays
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count=0
        for i in arr1:
            flag=False
            for j in arr2:
                if abs(i-j)<=d:
                    flag=True
            if flag==False:
                count+=1
        return count
        
