class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        visited, maxArea = set(), 0

        def outBound(row, col):
            if row < 0  or row >= n or col < 0 or col >= m or (row, col) in visited or grid[row][col] == 0:
                return True

        def dfs(row, col):
            if outBound(row, col):
                return 0
            visited.add((row, col))
            area = 1
            for i, j in dir:
                area += dfs(row + i, col + j)

            return area

        
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j]:
                    maxArea = max(maxArea, dfs(i, j))
        
        return maxArea

