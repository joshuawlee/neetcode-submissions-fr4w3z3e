"""
U: given a string you are trying to find the longest substring that 
doesn't have duplicate chars. duplicate chars meaning any repeated chars
input: string
output: length of longest substring without dup chars
edge cases:
- empty string
    - return 0
- all same chars
    - return 1

m: sliding window

p:
- create counter var and l & r pointers starting at beginning
- loop until right pointer is at end of string
    - create hash set to check for dup chars
    - slide r pointer down and check if new char is not dup with set
    - if a dup char is found reset counter and set
    - else store store the counter and check if its greater than max

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        dups = {}

        for r in range(len(s)):
            if s[r] in dups:
                l = max(dups[s[r]] + 1, l)
            dups[s[r]] = r
            res = max(res, r-l+1)

        return res



            
        