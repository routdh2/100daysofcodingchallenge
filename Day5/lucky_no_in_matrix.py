#Problem Statement: https://leetcode.com/problems/lucky-numbers-in-a-matrix
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result=[]
        for row in matrix:
            row_min=min(row)
            col_index=row.index(row_min)
            isMax=True
            for row2 in matrix:
                if row_min<row2[col_index]:
                    isMax=False
            if isMax==True:
                result.append(row_min)
        return result
        
