class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        indegree = defaultdict(int)
        ancestors = defaultdict(set)

        for frm, to in edges:
            graph[frm].append(to)
            indegree[to] += 1
        
        queue = deque()
        for i in range(n):
            if i not in indegree:
                queue.append(i)
        
        while queue:
            anc = queue.popleft()
            for dec in graph[anc]:
                indegree[dec] -= 1
                ancestors[dec] = ancestors[dec].union(ancestors[anc])
                ancestors[dec].add(anc)
                if indegree[dec] == 0:
                    queue.append(dec)
        
        return [sorted(ancestors[i]) for i in range(n)]
