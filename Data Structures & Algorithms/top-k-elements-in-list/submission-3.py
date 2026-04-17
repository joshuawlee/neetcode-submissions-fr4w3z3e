"""
U: find the k most frequent nums in an array 
input: array of integers and an int value of k
output: an array of k most frequent nums
edge cases:
- empty array 
- multiple nums of same frequencies (return first one to appear?)

m: min heap

p: first run nums array through a hash map to track occurences and values
then create min heap with that hash map and only store k values in the 
min heap by the occurences which leaves only the k most frequent nums 
in the min heap

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create count, value hash map
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #create min heap and only store up to k values
        minHeap = []
        for num in count.keys():
            heapq.heappush(minHeap, (count[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        #build return array by popping values in min heap
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res