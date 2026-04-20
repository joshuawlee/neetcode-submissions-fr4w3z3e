"""
U: given an int array find all of the unique triplets that sum to 0
input: int array
output: array of unique triplets that sum to 0
edge cases:
- empty array
- none sum to 0

m: two pointers

p:
- sort values in array to allow for two pointer property 
- loop through the values of the array setting them as the first value
    - set l and r pointers after set value
        - move pointer based on sum value
            - if sum less than 0 move l pointer
            - if sum greater than 0 move r pointer
    - if sum = 0 add triplet to res
        - increment the l pointer until there is no dup to ensure 
        unique triplets

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        #enumerate to use index and value
        for i, a in enumerate(nums):
            #early return
            if a > 0:
                break
            
            if i > 0 and nums[i-1] == a:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = a + nums[l] + nums[r]

                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                elif currSum == 0:
                    res.append([a, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
            

