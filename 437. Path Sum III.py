# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self. paths = 0

        def checkPath(root, curr):
            if not root:
                return 
            if targetSum == curr + root.val:
                self.paths += 1
            checkPath(root.left, curr + root.val)
            checkPath(root.right, curr + root.val) 
        

        def dfs(root):
            if not root:
                return 
            # check if we can get a path with a sum equals targetSum
            checkPath(root, 0)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return self.paths
