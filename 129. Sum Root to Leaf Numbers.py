# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        def dfs(root, num):
            currSum = 0
            if root.left:
                currSum += dfs(root.left, num * 10 + root.val)
            if root.right:
                currSum += dfs(root.right, num * 10 + root.val) 
                
            return currSum if currSum else num * 10 + root.val
        
        return dfs(root,0)

       
            
