'''Problem Statement: https://leetcode.com/contest/weekly-contest-184/problems/string-matching-in-an-array/'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result=set()
        for i in words:
            for j in words:
                if i!=j and i in j:
                    result.add(i)
        return result
