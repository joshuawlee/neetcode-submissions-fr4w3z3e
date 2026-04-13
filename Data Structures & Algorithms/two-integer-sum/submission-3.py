class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, n in enumerate(nums):
            numbers[n] = i #set value as key for indicies
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numbers and numbers[diff] != i:
                return [i, numbers[diff]]
        
        return []