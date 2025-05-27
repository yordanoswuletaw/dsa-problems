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
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dSet = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    dSet.union(i, j)
        
        rootStones = set()
        for i in range(n):
            rootStones.add(dSet.find(i))
        
        return len(stones) - len(rootStones)