# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(None)
        dummy.next = head

        prev = dummy
        for i in range(1, left):
            prev = prev.next
        
        curr = prev.next
        for i in range(0, right - left):
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next

        return dummy.next
