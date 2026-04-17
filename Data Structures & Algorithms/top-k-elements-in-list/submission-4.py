"""
optimize solution with bucket sort to get O(nlogk) -> O(n)

p:
- build frequency hash map to count how many times a number appears 
- create list of buckets for number of frequencies 
- loop through each number and frequency then add to list of buckets
- build result list by looping through highest freq k times
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []
        #build freq buckets
        for i in range(len(nums) + 1):
            freq.append([])

        #build counter map
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        #add numbers to the freq buckets
        for num, count in count.items():
            freq[count].append(num)

        #build res 
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                
                #stop once list has k elements
                if len(res) == k:
                    return res
            
        


        
        