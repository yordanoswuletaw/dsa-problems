class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        n = len(quiet)
        graph, indegree = defaultdict(list), defaultdict(int)

        for r1, r2 in richer:
            graph[r1].append(r2)
            indegree[r2] += 1
        
        ans = []
        queue = deque()
        for i in range(n):
            ans.append((i, quiet[i]))
            if i not in indegree:
                queue.append(i)
        
        while queue:
            person = queue.popleft()
            for nxt in graph[person]:
                indegree[nxt] -= 1
                if ans[person][1] < ans[nxt][1]:
                    ans[nxt] = ans[person]
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return [person for person, quietness in ans]


        


