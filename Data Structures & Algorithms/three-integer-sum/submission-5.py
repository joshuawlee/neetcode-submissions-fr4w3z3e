"""
u: find all sums of three numbers in an array that equal to 0 where each 
index is distinct
input: num array 
output: array of triplets that sum to 0
edge cases: 
- none of them sum to 0 
- empty array

m: two pointers

p:
- sort the array so that you can check which pointer you need to move
- enumerate the list of sorted nums to go through and skip duplicates
- once you find unique numbers
    - if sum is less than 0 incr l
    - if sum is greater than 0 decr r
    - add any valid sums into res


"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            #skip dup vals
            if i > 0 and a == nums[i-1]:
                continue 

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
        
        return res
