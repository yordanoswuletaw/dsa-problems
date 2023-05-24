class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        queue = deque()
        direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minMinutes, notRotted = 0, 0

        # finding one rotted orange
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    notRotted += 1


        def outBound(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or (x, y) in visited or grid[x][y] != 1:
                return True

        while queue and notRotted > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for _x, _y in direc:
                    newX = x + _x 
                    newY = y + _y
                    if outBound(newX, newY):
                        continue
                
                    grid[newX][newY] = 2
                    queue.append((newX, newY))
                    notRotted -= 1

            minMinutes += 1

        return -1 if notRotted else minMinutes

