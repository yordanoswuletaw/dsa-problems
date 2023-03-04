# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        
        odd, even = head, head.next

        while even and even.next:
            nxt = even.next
            even.next = nxt.next
            nxt.next = odd.next
            odd.next = nxt
            odd, even = nxt, even.next

        return head
