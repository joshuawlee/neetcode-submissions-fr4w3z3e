class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0

        for price in prices:
            if price < buy:
                buy = price
            if price - buy > maxProfit:
                maxProfit = price - buy


        return maxProfit