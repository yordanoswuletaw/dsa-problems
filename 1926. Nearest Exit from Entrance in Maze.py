class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        n, m = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set([(entrance[0], entrance[1])])
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isExit(x, y):
            if [x, y] != entrance and (x == 0 or x == n - 1 or y == 0 or y == m - 1):
                return True

        def inBound(x, y):
            if 0 <= x < n and 0 <= y < m and maze[x][y] == '.' and (x,y) not in visited:
                return True

        while queue:
            x, y, step = queue.popleft()
            if isExit(x, y):
                return step

            for i, j in direc:
                _x, _y = x + i, y + j
                if inBound(_x, _y):
                    queue.append((_x, _y, step + 1))
                    visited.add((_x, _y))
        
        return -1

