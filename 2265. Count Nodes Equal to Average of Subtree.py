# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def countEquals(root):
            nonlocal res
            if not root:
                return (0,0)
            
            leftSum, leftCount = countEquals(root.left)
            rightSum, rightCount = countEquals(root.right)

            currSum, currCount = root.val + leftSum + rightSum, 1 + leftCount + rightCount
            
            if currSum // currCount == root.val:
                res += 1
            return (currSum, currCount)
        countEquals(root)
        return res





