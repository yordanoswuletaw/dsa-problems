class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adjList = defaultdict(list)
        for src, dest in dislikes:
            adjList[src].append(dest)
        
        def dfs(v):
            for ngbr in adjList[v]:
                if ngbr in colors:
                    if colors[ngbr] == colors[v]:
                        return False
                else:
                    colors[ngbr] = 1 - colors[v]
                    if not dfs(ngbr):
                        return False
            return True

        
        for v in range(1, n + 1):
            colors = {}
            if v not in colors:
                colors[v] = 1
                if not dfs(v):
                    return False
        return True

        
