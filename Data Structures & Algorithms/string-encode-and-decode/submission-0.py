"""
u: encode the string but in a way that you can decode it to be the 
same original string
input: string
output: same string
edge cases:
- empty string
- delimiter is in the string ("#")

m: length pre-fixing

p: 
- encode the string by adding the length of the original string and 
a delimiter to the string and build a long string to send to decoder
- decode the long string by looping until you find the delimtier that 
serves as the start of the string then extract the lenght you added
to the encoded string and build a string from there using the length
- add each word to list of strings

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            word = s[j+1 : j + 1 + length]
            res.append(word)

            i = j + 1 + length
        
        return res
