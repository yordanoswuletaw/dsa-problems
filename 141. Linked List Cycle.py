# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False
        
        slow = fast = head
        while fast and fast.next:
            '''
            if there is a loop in the list at some point the fast pointer will reach
            the slower pointer 
            '''
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        
        return False


        
