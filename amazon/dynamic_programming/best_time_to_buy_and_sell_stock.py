# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    
    def maxProfit(self, prices):
        max_profit = 0
        min_price = float('inf')
        test = []
        test.appendl
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        
        return max_profit