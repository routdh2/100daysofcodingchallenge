#Problem Statement:https://leetcode.com/problems/count-primes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        nums=[True]*n
        nums[0]=nums[1]=False
        i=2
        while i<(n**0.5):
            j=2
            if nums[i]==True:
                while i*j<n:
                    if nums[i*j]==True:
                        nums[i*j]=False
                    j+=1
            i+=1
        count=0
        for i in nums:
            if i==True:
                count+=1
        return count
