class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        def in_bound(x, y):
            return 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited

        direc = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
        # initalize queue with source node and initial path
        queue = deque([(0,0,1)])
        visited = set([(0,0)])
        while queue:
            for _ in range(len(queue)):
                x, y, path = queue.popleft()
                if x == n - 1 == y:
                    return path
                for i, j in direc:
                    new_x, new_y = x + i, y + j
                    if in_bound(new_x, new_y):
                        queue.append((new_x, new_y, path + 1))
                        visited.add((new_x, new_y))
        
        return -1
                
        