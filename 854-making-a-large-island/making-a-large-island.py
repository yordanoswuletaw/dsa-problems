class UnionFind:
    
    def __init__(self, n: int):
        self.root = {i: i for i in range(n)}
        self.size = [1] * n
    
    def find(self, node: int):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, node1: int, node2: int):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if self.size[root2] > self.size[root1]:
            self.root[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.root[root2] = root1
            self.size[root1] += self.size[root2]
    
    def connected(self, node1: int, node2: int):
        return self.find(node1) == self.find(node2)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        djSet = UnionFind(n * n)
        direc = [(1,0), (-1,0), (0,1), (0,-1)]
        ones = []
        zeros = []

        def flatten(x, y):
            return x * n + y

        def inbound(x, y):
            return 0 <= x < n and 0 <= y < n and grid[x][y]

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    ones.append((i, j))
                else:
                    zeros.append((i, j))
        
        if not zeros:
            return n * n
        elif not ones:
            return 1

        for x, y in ones:
            for i, j in direc:
                new_x = x + i
                new_y = y + j
                if inbound(new_x, new_y):
                    node1, node2 = flatten(x, y), flatten(new_x, new_y)
                    if djSet.find(node1) != djSet.find(node2):
                        djSet.union(node1, node2)
        size = 0
        for x, y in zeros:
            parents = set()
            for i, j in direc:
                new_x = x + i
                new_y = y + j
                if inbound(new_x, new_y):
                    parents.add(djSet.find(flatten(new_x, new_y)))
            curr_size = 1
            for parent in parents:
                curr_size += djSet.size[parent]
            size = max(size, curr_size)

        return size      