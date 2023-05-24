class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        direc = [(1, 1), (0, 1), (1, 0), (-1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1)]

        if grid[0][0]:
            return -1
        
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        clearPath = 1

        def inBound(x, y):
            if 0 <= x < n and 0 <= y < n and (x, y) not in visited and grid[x][y] == 0:
                return True

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == n - 1 == y:
                    return clearPath
                for _x, _y in direc:
                    newX = x + _x
                    newY = y + _y
                    if inBound(newX, newY):
                        visited.add((newX, newY))
                        queue.append((newX, newY))
                        
            clearPath += 1
        
        return -1
