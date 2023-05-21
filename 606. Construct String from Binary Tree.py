# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
       
        if root.left and root.right:
            return str(root.val) + '(' + self.tree2str(root.left) + ')' + '(' + str(self.tree2str(root.right)) + ')'
        elif root.left:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'
        elif root.right:
            return str(root.val) + '()(' + self.tree2str(root.right) + ')'
        else:
            return str(root.val)
