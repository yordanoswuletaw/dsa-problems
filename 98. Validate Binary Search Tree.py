# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def inorder(root):
            if root:
                return inorder(root.left) + [root.val] + inorder(root.right)
            return []
        
        arr, indx = inorder(root), 1
       
        while indx < len(arr):
            if arr[indx] <= arr[indx - 1]:
                return False 
            indx += 1
        return True
