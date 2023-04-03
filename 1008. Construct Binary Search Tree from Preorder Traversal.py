# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        root  = None
        for val in preorder:
            if root:
                prev = None
                curr = root
                while curr:
                    prev = curr
                    if curr.val > val:
                        curr = curr.left
                    else:
                        curr = curr.right
                if prev.val > val:
                    prev.left = TreeNode(val)
                else:
                    prev.right = TreeNode(val)
            else:
                root  = TreeNode(val)
        return root
