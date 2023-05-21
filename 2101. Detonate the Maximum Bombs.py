class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        n = len(bombs)
        adjList = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j:
                    x = abs(bombs[i][0] - bombs[j][0]) ** 2
                    y = abs(bombs[i][1] - bombs[j][1]) ** 2
                    dist = (x + y) ** 0.5
                    if dist <= bombs[i][2]:
                        adjList[i].append(j)
        
        maxDetonation = 0

        def dfs(v, visited):
            visited.add(v)
            for ngbr in adjList[v]:
                if ngbr not in visited:
                    dfs(ngbr, visited)

            return len(visited)
        
        for v in range(n):
            visited = set()
            maxDetonation = max(maxDetonation, dfs(v, visited))
        
        return maxDetonation
        
