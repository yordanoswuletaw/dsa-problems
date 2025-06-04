# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue1 = deque([root])
        queue2 = deque()
        zigzag_level = []
        while queue1 or queue2:
            curr_nodes = []
            if queue1:
                for _ in range(len(queue1)):
                    node = queue1.popleft()
                    curr_nodes.append(node.val)
                    if node.left:
                        queue2.append(node.left)
                    if node.right:
                        queue2.append(node.right)
                zigzag_level.append(curr_nodes)
            elif queue2:
                for _ in range(len(queue2)):
                    node = queue2.pop()
                    curr_nodes.append(node.val)
                    if node.right:
                        queue1.appendleft(node.right)
                    if node.left:
                        queue1.appendleft(node.left)
                zigzag_level.append(curr_nodes)

        return zigzag_level