class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        n, m = len(mat), len(mat[0])
        queue = deque()
        result = [[-1 for i in range(m)] for j in range(n)]
        direc = ((1,0), (-1,0), (0,1), (0,-1))

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    result[i][j] = 0
        
        def inBound(x, y):
            if 0 <= x < n and 0 <= y < m and result[x][y] == -1:
                return True
        
        while queue:
            x, y = queue.popleft()
            for i, j in direc:
                _x, _y = x + i, y + j
                if inBound(_x, _y):
                    result[_x][_y] = 1 + result[x][y]
                    queue.append((_x, _y))
        
        return result
