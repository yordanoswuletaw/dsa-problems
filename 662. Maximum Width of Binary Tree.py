# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        positions = defaultdict(lambda:  float('inf'))
        self.maxWidth = 0

        def dfs(root, level, pos):
            if not root:
                return 

            # computing the current width
            positions[level] = min(positions[level] , pos)
            self.maxWidth = max(self.maxWidth, pos - positions[level] + 1)

            # and we know that starting from root the left is 2 * currPos away and right is 2 * currPos + 1 away
            dfs(root.left, level + 1,  pos * 2)
            dfs(root.right, level + 1, pos * 2 + 1)
        
        dfs(root, 0, 0)
        
        return self.maxWidth
    
