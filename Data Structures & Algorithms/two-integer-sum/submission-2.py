class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, num in enumerate(nums):
            numbers[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in numbers and numbers[diff] != i:
                return [i, numbers[diff]]
        return []
        