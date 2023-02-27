# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        output = self.checkPalindrome(head, head)
        return output[1]

    def checkPalindrome(self, head, right) -> bool:

        if right:
            left, res = self.checkPalindrome(head, right.next) 
            return left.next, left.val == right.val and res

        return head, True
