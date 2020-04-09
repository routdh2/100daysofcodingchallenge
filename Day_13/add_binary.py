'''Problem Statement: https://leetcode.com/problems/add-binary'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        smaller,bigger=(a,b) if len(a)<len(b) else (b,a)
        smaller=smaller.zfill(len(bigger))
        index=len(bigger)-1
        carry=0
        result=[]
        while index>=0:
            sum=int(smaller[index])+int(bigger[index])+carry
            result.append(str(sum%2))
            carry=sum//2
            index-=1
        if carry==1:
            result.append(str(carry))
        result.reverse()
        return "".join(result)
        
