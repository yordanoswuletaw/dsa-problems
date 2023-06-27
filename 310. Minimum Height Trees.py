class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        graph, degree = defaultdict(list), defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        queue, stack = deque(), []
        for i in range(n):
            if degree[i] == 1:
                queue.append((i, 0))
        
        while queue:
            node, height = queue.popleft()
            while stack and stack[-1][1] < height:
                stack.pop()
            stack.append((node, height))
            for nxt in graph[node]:
                degree[nxt] -= 1
                if degree[nxt] == 1:
                    queue.append((nxt , height + 1))
        
        return [node for node, height in stack]
