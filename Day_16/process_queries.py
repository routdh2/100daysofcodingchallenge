'''Problem Statement: https://leetcode.com/contest/weekly-contest-184/problems/queries-on-a-permutation-with-key/'''
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm=[]
        for i in range(1,m+1):
            perm.append(i)
        result=[]
        for item in queries:
            index=perm.index(item)
            result.append(index)
            perm.remove(item)
            perm.insert(0,item)
        return result
            
        
