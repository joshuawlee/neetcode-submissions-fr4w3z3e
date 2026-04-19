"""
u: find the max area given an array of heights. the area is 
h (min) * width. use the shorter height between the two bars to calc
then width is diff of indicies
input: array of heights
output: max area 
edge cases:
- empty list (return 0)

m: two pointers, greedy

p: 
- start with max width (set pointers at beginning and end)
- greedy since yk that you want to max area move the shorter height
- keep track of max area and upate when necessary

"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)

            if area > maxWater:
                maxWater = area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxWater
        