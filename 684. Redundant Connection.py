class UnionFind:

    def __init__(self, n: int):
        self.root = {i: i for i in range(n)}
        self.size = [1] * n
    
    def find(self, node1: int):
        if node1 == self.root[node1]:
            return node1
        self.root[node1] = self.find(self.root[node1])
        return self.root[node1]
    
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        dSet = UnionFind(len(edges) + 1)
        for x, y in edges:
            if dSet.connected(x, y):
                return [x, y]
            else:
                dSet.union(x, y)
