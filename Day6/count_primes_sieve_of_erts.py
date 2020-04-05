#Problem Statement:https://leetcode.com/problems/count-primes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        nums=[1]*n
        nums[0]=nums[1]=0
        for i in range(2,int(n**0.5)+1):
            if nums[i]==1:
                for j in range(i*i,n,i):
                    nums[j]=0
        return sum(nums)
