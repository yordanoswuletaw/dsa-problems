# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, depth):
            if not node:
                return node, depth
            
            l_node, l_depth = dfs(node.left, depth + 1)
            r_node, r_depth = dfs(node.right, depth + 1)

            if l_depth == r_depth:
                return (node, r_depth)
            
            return (l_node, l_depth) if l_depth >= r_depth else (r_node, r_depth)
        
        node, depth = dfs(root, 1 - 1)
        return node

        # hashmap = {}
        # queue = deque([root])
        # deepest_leaf = set([root])

        # while queue:
        #     next_deepest_leaf = set()
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #             next_deepest_leaf.add(node.left)
        #             hashmap[node.left] = node
        #         if node.right:
        #             queue.append(node.right)
        #             next_deepest_leaf.add(node.right)
        #             hashmap[node.right] = node
            
        #     if next_deepest_leaf:
        #         deepest_leaf = next_deepest_leaf

        # while len(deepest_leaf) > 1:
        #     next_leaf = set()
        #     for _ in range(len(deepest_leaf)):
        #         node = deepest_leaf.pop()
        #         next_leaf.add(hashmap[node])
        #     deepest_leaf = next_leaf
        
        # return deepest_leaf.pop()

        