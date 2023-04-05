# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        hashMap = defaultdict(dict)

        def verticalOrder(root, row, col):
            if not root:
                return
            verticalOrder(root.left, row + 1, col - 1)
            # storing each nodes value based on it's column and row for later sorting
            if row in hashMap[col]:
                hashMap[col][row].append(root.val)
            else:
                hashMap[col][row] = [root.val]
            verticalOrder(root.right, row + 1, col + 1)

        verticalOrder(root, 0, 0)

        res = []
        for key in sorted(hashMap):
            curr = []
            for subKey in sorted(hashMap[key]):
                curr += sorted(hashMap[key][subKey])
            res.append(curr)

        return res
