# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: 

        hashSet = set()
        ptr = head

        while ptr:
            if ptr in hashSet:
                return ptr
            hashSet.add(ptr)
            ptr = ptr.next
        
        return None
