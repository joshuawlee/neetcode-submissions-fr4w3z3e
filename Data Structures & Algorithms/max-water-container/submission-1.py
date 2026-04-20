"""
U: You are given an array that stores heights of different bars and you
are trying to find the max area that can be formed considering area is
w * h where w is the diff between the indicies and h is the value at
heights[i]
input: int array of heights
output: max area 
edge cases:
- empty array

m: greedy (always move shorter height), two pointer

p:
- set two pointers at the max width (beginning and end)
- loop until the pointers touch 
    - calculate the curr area 
        - if larger than the curr max replace
    - move the pointer to the shorter height in order to maximize area
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1

        while l < r:
            currMax = min(heights[l], heights[r]) * (r-l)

            if currMax > maxWater:
                maxWater = currMax
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater