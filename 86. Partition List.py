# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        less = ltail = ListNode(None)
        greater = gtail = ListNode(None)

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                gtail.next = head
                gtail = gtail.next
            head = head.next

        # appending less and greater linkedlist
        ltail.next = greater.next
        # free the last node's next value to prevent from creating circular linkedlist
        gtail.next = None

        return less.next
