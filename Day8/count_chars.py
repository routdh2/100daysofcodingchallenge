'''Problem Statement: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters'''
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic={}
        for char in chars:
            dic[char]=1+dic.get(char,0)
        total_len=0
        for word in words:
            flag=True
            for char in word:
                if char in dic:
                    if word.count(char)<=dic.get(char):
                        pass
                    else:
                        flag=False
                        break
                else:
                    flag=False
                    break
            if flag==True:
                total_len+=len(word)
        return total_len
            
        
