'''Problem Statement: https://leetcode.com/problems/unique-number-of-occurrences'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for i in arr:
            dic[i]=1+dic.get(i,0)
        if len(dic.values())==len(set(dic.values())):
            return True
        else:
            return False
