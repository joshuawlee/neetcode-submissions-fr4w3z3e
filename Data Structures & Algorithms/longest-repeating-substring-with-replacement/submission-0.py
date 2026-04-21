"""
u: given a string you can change up to k chars to make a substring of
repeating chars. find the largest substring of repeating chars
input: string of uppercase chars, # of replacements
output: max length of substring of repeating chars
edge cases:
- empty string
    - return 0
- k = 0 
    - return len

m: sliding window

p:
- 
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = {}
        maxF = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])

            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res