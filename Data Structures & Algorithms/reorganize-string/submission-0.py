"""
u: rearrange a given string to that there are no repeated adjacent chars
input: string of chars
output: string of chars without adjacet dups
edge cases:
- empty string (return "")
- 1 char string (return 1 char)

m: greedy approach (freq map)

p: using greedy approach map out freq of chars in s then find the most
frequent char to map out first. if the max frequency is greater than 
half of the string size early fail. if not map out the char in the 
string for every i+2 index. then fill in the rest with the other chars.
if you hit the end then go through odd i's.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        #map out freq of chars
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        #check early return
        maxIdx = freq.index(max(freq))
        maxFreq = freq[maxIdx]
        if maxFreq > (len(s) + 1) // 2:
            return ""

        #build res 
        res = [''] * len(s)
        idx = 0
        maxChar = chr(maxIdx + ord('a'))

        #map maxChar first greedily
        while freq[maxIdx] > 0:
            res[idx] = maxChar
            idx += 2
            freq[maxIdx] -= 1
        
        #fill in rest of res
        for i in range(26): #loop through alphabet
            while freq[i] > 0: #fill in all of each char
                if idx >= len(s):
                    idx = 1
                
                res[idx] = chr(i + ord('a'))
                freq[i] -= 1
                idx += 2
        
        #build res into string
        return ''.join(res)

        