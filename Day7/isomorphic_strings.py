'''Problem Statement: https://leetcode.com/problems/isomorphic-strings'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1={}
        for i,j in zip(s,t):
            if i not in dic1:
                if j in dic1.values():
                    return False
                else:
                    dic1.update({i:j})
            elif dic1.get(i)!=j:
                return False
        return True
                
        
