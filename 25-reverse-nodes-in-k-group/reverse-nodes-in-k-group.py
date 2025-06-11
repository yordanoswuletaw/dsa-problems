# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
    
        head = dummy = ListNode(None, head)
        start = head.next
        for _ in range(n//k):
            prev, curr = start, start.next
            t = k
            while t > 1 and curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                t -= 1
            start.next = curr
            dummy.next = prev
            dummy = start
            start = curr

        return head.next
