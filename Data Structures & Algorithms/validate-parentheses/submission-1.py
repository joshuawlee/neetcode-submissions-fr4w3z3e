"""
u: given a combination of (){}[] you want to see if they are valid 
input: string of (){}[]
output: bool if valid
edge cases:
- empty string
    - return true

m: stack

p:
- if an open symbol add to stack 
- if a close symbol check if there is an matching open symbol then pop
"""

class Solution:
    def isValid(self, s: str) -> bool:
        key = {')': '(', '}' : '{', ']' : '['}
        stack = []

        for c in s:
            if c in key:
                if stack and stack[-1] == key[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
    
