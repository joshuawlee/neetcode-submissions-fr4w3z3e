"""
u: for each index of the resulting array it should be the sum of all 
elements not at i 
input: array of ints
output: resulting sums array
edge cases:
- empty list

m: prefix postfix

p:
- create an array to store the values
- calculate prefix values at each index by incrementing from beg to end
    - add them to the res array
- calculate postfix values at each index by incrementing from end to beg
    - multiply them with the prefix values at each index
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        

        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= postfix
            postfix = postfix * nums[i]
        
        return res