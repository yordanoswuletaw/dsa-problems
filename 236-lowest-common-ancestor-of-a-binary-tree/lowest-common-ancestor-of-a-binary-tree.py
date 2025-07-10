# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, alarm1, alarm2):
            if root is None:
                return False
                
            count = 1 if root == alarm1 or root == alarm2 else 0
            a = dfs(root.left, alarm1, alarm2)
            if a is True:
                count += 1
            elif a:
                return a
            b = dfs(root.right, alarm1, alarm2)
            if b is True:
                count += 1
            elif b:
                return b

            # for childAlarm in root.childAlarms:
            #     result = dfs(childAlarm, alarm1, alarm2)
            #     if result == True:
            #         count += 1
            #     elif result is CompositeAlarm:
            #         return result
            #     if count == 2:
            #         break
            
            if count == 2:
                return root 
                
            if count == 1:
                return True
                
            return False
        
        result = dfs(root, p, q)
        print(result)
        if result is not True and result:
            return result
            
        return None
            
        