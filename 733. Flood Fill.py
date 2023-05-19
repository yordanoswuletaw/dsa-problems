class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        n, m = len(image), len(image[0])
        dir = [(-1, 0), (1, 0), (0,-1), (0, 1)]
        visited = set()
        floodColor = image[sr][sc]

        def inBound(row, col):
            if 0 <= row < n and 0 <= col < m and (row, col) not in visited and image[row][col] == floodColor:
                return True 

        def dfs(row, col):
            if not inBound(row, col):
                return 
            
            visited.add((row, col))
            image[row][col] = color
            for i, j in dir:
                dfs(row + i, col + j) 
        
        dfs(sr, sc)

        return image


