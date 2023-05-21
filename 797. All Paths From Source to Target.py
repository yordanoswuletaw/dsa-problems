class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph)
        src, dest = 0, n - 1
        paths = []
        
        def dfs(v, path):
            path.append(v)
            if v == dest:
                paths.append(path[:])

            for ngbr in graph[v]:
                dfs(ngbr, path)

            path.pop()
        
        dfs(src, [])
        return paths

        
