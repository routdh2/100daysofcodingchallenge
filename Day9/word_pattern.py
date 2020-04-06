'''Problem Statement: https://leetcode.com/problems/word-pattern'''
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        dic={}
        words=str.split()
        if(len(pattern)!=len(words)):
            return False
        for i in range(0,len(words)):
            key=pattern[i]
            if key in dic:
                if dic.get(key)!=words[i]:
                    return False
            else:
                if words[i] in dic.values():
                    return False
                else:
                    dic.update({key:words[i]})
        return True
                
        
