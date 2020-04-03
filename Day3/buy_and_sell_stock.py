#Problem Statement: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        min_price=prices[0]
        max_profit=0
        for value in prices:
            if value<min_price:
                min_price=value
            else:
                profit=value-min_price
                if profit>max_profit:
                    max_profit=profit
        return max_profit
