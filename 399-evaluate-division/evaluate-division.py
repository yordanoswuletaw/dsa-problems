class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        n, m = len(equations), len(queries)
        graph = defaultdict(list)
        degree = defaultdict(int)
        for i in range(n):
            u, v = equations[i]
            val = values[i]
            graph[u].append((v, val))
            degree[u] += 1
            graph[v].append((u, 1/val))
            degree[v] += 1
        
        ans = []

        for u, v in queries:
            if u not in graph or v not in graph:
                ans.append(-1.0)
                continue
            queue = deque([(u, 1)])
            temp_degree = degree.copy()
            while queue:
                x, val = queue.popleft()
                if x == v:
                    ans.append(val)
                    break
                for nb, sc in graph[x]:
                    if temp_degree[nb] > 0:
                        queue.append((nb, sc * val))
                        temp_degree[nb] -= 1
            else:
                ans.append(-1.0)
        
        return ans