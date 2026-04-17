class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numDict:
                return [numDict[diff], i]
            numDict[n] = i
        
        return []