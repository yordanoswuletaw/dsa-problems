class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = defaultdict(list)
        visited = set()

        for c1, c2 in prerequisites:
            adjList[c1].append(c2)
        
        def dfs(vertix):
            if vertix in visited:
                return False 
            
            visited.add(vertix)
            for cource in adjList[vertix]:
                if not dfs(cource):
                    return False

            visited.remove(vertix)
            adjList[vertix] = []
            return True
        
        for c1, c2 in prerequisites:
            if c1 not in visited:
                if not dfs(c1):
                    return False
                
        return True
