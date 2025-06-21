# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
     
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        hash_map = defaultdict(ListNode)
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i))
                hash_map[i] = node

        head = curr = ListNode(None)
        while heap:
            _, i = heapq.heappop(heap)
            node = hash_map[i]
            curr.next = node
            curr = curr.next
            node = node.next
            curr.next = None
            if node:
                heapq.heappush(heap, (node.val, i))
                hash_map[i] = node
        
        return head.next
        