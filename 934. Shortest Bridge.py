class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)
        visited = set()
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, visited):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] == 0 or (x, y) in visited:
                return 
            visited.add((x, y))
            for i, j in direc:
                dfs(x + i, y + j, visited)
        
        for i,row in enumerate(grid):
            if 1 in row:
                j = row.index(1)
                dfs(i, j, visited)
                break
        
        def inBound(x, y):
            if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                return True 
        
        queue = deque(visited)
        flips = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for i, j in direc:
                    _x, _y = x + i, y + j
                    if inBound(_x, _y):
                        if grid[_x][_y] and (_x, _y) not in visited:
                            return flips
                        queue.append((_x, _y))
                        visited.add((_x, _y))
            flips += 1
        


            
