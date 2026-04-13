class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1 = []

        for num in nums:
            if num in map1:
                return True
            else:
                map1.append(num)
        return False
