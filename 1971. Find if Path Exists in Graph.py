class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        visited = set([source])
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        # bfs
        queue = deque([source])
        while queue:
            v = queue.popleft()
            if v == destination:
                return True 
            for neib in graph[v]:
                if neib not in visited:
                    queue.append(neib)
                    visited.add(neib)

        return False 


        # dfs iterative approach
        stack = [source]
        while stack:
            top = stack.pop()
            if top == destination:
                return True 
            for each in graph[top]:
                if each not in visited:
                    stack.append(each)
                    visited.add(each)
        
        return False 

        # dfsrecursive approach
        def dfs(vertix, visited):
            if vertix in visited:
                return
            if vertix == destination:
                return True
            
            visited.add(vertix)
            for each in graph[vertix]:
                if dfs(each, visited):
                    return True 
        
        return dfs(source, set())
        
