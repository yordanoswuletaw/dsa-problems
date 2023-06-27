# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # using heap
        head = ptr = ListNode(None)
        heap = []
        for each in lists:
            if each:
                curr = each
                while curr:
                    heap.append(curr.val)
                    curr = curr.next

        heapify(heap)
        while heap:
            ptr.next = ListNode(heappop(heap))
            ptr = ptr.next

        return head.next

        # devide and conquer
    #     if len(lists) < 1:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #     mid = len(lists) // 2
    #     left = self.mergeKLists(lists[:mid])
    #     right = self.mergeKLists(lists[mid:])
    #     return self.merge(left,right)

    # def merge(self, left, right):
    #     dummyNode = tail = ListNode(None)
    #     while left and right:
    #         if left.val <= right.val:
    #             tail.next = left
    #             left = left.next
    #         else:
    #             tail.next = right
    #             right = right.next
    #         tail = tail.next
    #     if left:
    #         tail.next = left
    #     elif right:
    #         tail.next = right
    #     return dummyNode.next
