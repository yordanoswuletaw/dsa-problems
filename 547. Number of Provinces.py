class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n, m = len(isConnected), len(isConnected[0])
        adjList = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if isConnected[i][j]:
                    if i != j:
                        adjList[i].append(j)
                    elif i not in adjList:
                        adjList[i] = []

        visited = set()
        connected = 0

        def dfs(vertix):
            if vertix in visited:
                return 

            visited.add(vertix)    
            for neigbr in adjList[vertix]:
                dfs(neigbr)
        
        for vertix in adjList.keys():
            if vertix not in visited:
                dfs(vertix)
                connected += 1
        
        return connected
