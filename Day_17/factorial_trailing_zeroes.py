'''Problem Statement: https://leetcode.com/problems/factorial-trailing-zeroes'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        total=0
        while n!=0:
            total+=(n//5)
            n=n//5
        return total
        
