class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[-1])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        lands = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    lands.add((i, j))
        
        def inBound(x, y):
            return 0 <= x < n and 0 <= y < m and (x, y) in lands

        islands = 0
        while lands:
            land = lands.pop()
            queue = deque([land])
            while queue:
                i, j = queue.popleft()
                for x, y in directions:
                    new_i, new_j = i + x, j + y
                    if inBound(new_i, new_j):
                        lands.remove((new_i, new_j))
                        queue.append((new_i, new_j))

            islands += 1
        
        return islands