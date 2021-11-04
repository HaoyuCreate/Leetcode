class Solution:
    def maxProfit(self, prices) -> int:
        min_price = 1e4+1
        max_profit = 0
        for price in prices:
            if price<min_price:
                min_price = price
            max_profit = max(max_profit,price - min_price)
        return max_profit

