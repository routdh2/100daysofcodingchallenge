#Problem Statement: https://leetcode.com/problems/find-lucky-integer-in-an-array
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic={}
        for value in arr:
            if value in dic:
                dic[value]+=1
            else:
                dic.update({value:1})
        lucky_int=-1
        for key,value in dic.items():
            if key==value:
                if key>lucky_int:
                    lucky_int=key
        return lucky_int
        
