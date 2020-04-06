'''Problem Statement: https://leetcode.com/problems/maximum-number-of-balloons '''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic={}
        for char in text:
            dic[char]=1+dic.get(char,0)
        dic2={}
        for char in "balloon":
            dic2[char]=dic2.get(char,0)+1
        result=[]
        for key,value in dic2.items():
            if key in dic:
                result.append(dic.get(key)//value)
            else:
                return 0
        return min(result)
