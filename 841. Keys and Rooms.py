class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        graph = defaultdict(list)

        for i in range(n):
            graph[i] = rooms[i]
        
        unlocked = set([0])
        queue = deque([0])

        while queue:
            key = queue.popleft()
            for newKey in graph[key]:
                if newKey not in unlocked:
                    unlocked.add(newKey)
                    queue.append(newKey)
        
        return len(unlocked) == n
