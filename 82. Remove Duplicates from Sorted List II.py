# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = prev = ListNode(None, head)
        slow = fast = head

        while fast:
            # traversing through nodes that has the same value
            while fast and slow.val == fast.val:
                fast = fast.next

            # if there is duplicates
            if slow and slow.next is fast:
                prev.next = slow
                prev = slow
            slow = fast
        
        # to clean nodes if the list contains only duplicates only
        prev.next = fast

        return dummy.next
