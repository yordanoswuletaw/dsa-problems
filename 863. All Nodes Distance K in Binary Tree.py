# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)

        def buildGraph(parent, node):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
            if node.left:
                graph[node.val].append(node.left.val)
                buildGraph(node, node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                buildGraph(node, node.right)

        buildGraph(None, root)
        
        res = []
        visited = set()
        def dfs(v, count):
            if v in visited or count > k:
                return
            if count == k:
                res.append(v)
                return 
            visited.add(v)
            for nieb in graph[v]:
                dfs(nieb, count + 1)
        
        dfs(target.val, 0)
        return res

