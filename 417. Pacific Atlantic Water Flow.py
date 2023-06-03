class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pasific = set()
        atlantic = set()
        n, m = len(heights), len(heights[0])
        direc = ((1,0), (-1,0), (0,1), (0,-1))

        def inBound(x, y, _x, _y, ocean):
            if (_x, _y) not in ocean and 0 <= _x < n and 0 <= _y < m and heights[x][y] <= heights[_x][_y]:
                return True
        
        def bfs(queue, ocean):
            while queue:
                x, y = queue.popleft()
                for i, j in direc:
                    _x = x + i
                    _y = y + j
                    if inBound(x, y, _x, _y, ocean):
                        ocean.add((_x, _y))
                        queue.append((_x, _y))

        for i in range(m):
            # pasific
            if (0,i) not in pasific:
                pasific.add((0,i))
                queue = deque([(0, i)])
                bfs(queue, pasific)
            # atlantic
            if (n-1,i) not in atlantic:
                atlantic.add((n-1,i))
                queue = deque([(n-1, i)])
                bfs(queue, atlantic)

        for i in range(n):
            # pasific
            if (i, 0) not in pasific:
                pasific.add((i,0))
                queue = deque([(i,0)])
                bfs(queue, pasific)
            # atlantic
            if (i, m-1) not in atlantic:
                atlantic.add((i,m-1))
                queue = deque([(i,m-1)])
                bfs(queue, atlantic)

        return pasific.intersection(atlantic)


