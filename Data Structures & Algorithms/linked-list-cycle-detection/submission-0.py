# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
u: check if a linked list has a cycle in it
input: singly linked list
output: bool
edge cases:
- empty linked list
    - return false

m: slow, fast pointer

p:
- use slow, fast pointers and loop through list
    - if fast == slow then cycle 
    - if not then no cycle
"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
            
        return False