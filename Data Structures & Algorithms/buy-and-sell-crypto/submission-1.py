"""
u: you are given prices of stocks at different days where the index is
a day. you want to find the best time to buy and then sell the stock 
for the max profits
input: int array of prices on diff days
output: max proft you can get
edge cases:
- empty list
    - return 0
- descending list
    - return 0

m: sliding window

p: 
- set l and r pointers at beginning
- loop until l pointer hits end of list
    - increment r pointer 
        - if r is less than l move l to r to reset window
        - if r is greater than l calculate profit 
            - if profit is greater than currMax store it
            - else skip
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                curr = prices[r] - prices[l]
                maxProfit = max(curr, maxProfit)
            else:
                l = r
            r += 1
    
        return maxProfit

