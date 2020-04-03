#Problem statement: https://leetcode.com/problems/plus-one
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index=-1
        while index>=-len(digits):
            if digits[index]<9:
                digits[index]+=1
                return digits
            else:
                digits[index]=0
            index-=1
        digits.insert(0,1)
        return digits
