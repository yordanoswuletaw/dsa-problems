class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        adjList, degree = defaultdict(list), defaultdict(int)
        n = len(graph)
        queue = deque()
        ans = []
        for i  in range(n):
            edges = graph[i]
            if not edges:
                queue.append(i)
                continue
            for edge in edges:
                adjList[edge].append(i)
                degree[i] += 1
        
        while queue:
            v = queue.popleft()
            ans.append(v)
            for neib in adjList[v]:
                degree[neib] -= 1
                if degree[neib] == 0:
                    queue.append(neib)
        ans.sort()
        return ans
                

