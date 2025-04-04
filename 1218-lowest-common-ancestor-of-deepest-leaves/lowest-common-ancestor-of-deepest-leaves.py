# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        hashmap = {}
        queue = deque([root])
        deepest_leaf = set([root])

        while queue:
            next_deepest_leaf = set()
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    next_deepest_leaf.add(node.left)
                    hashmap[node.left] = node
                if node.right:
                    queue.append(node.right)
                    next_deepest_leaf.add(node.right)
                    hashmap[node.right] = node
            
            if next_deepest_leaf:
                deepest_leaf = next_deepest_leaf

        while len(deepest_leaf) > 1:
            next_leaf = set()
            for _ in range(len(deepest_leaf)):
                node = deepest_leaf.pop()
                next_leaf.add(hashmap[node])
            deepest_leaf = next_leaf
        
        return deepest_leaf.pop()

        