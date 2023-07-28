class UnionFind:

    def __init__(self):
        self.root = {char: char for char in string.ascii_lowercase}
    
    def find(self, char: string):
        if char == self.root[char]:
            return char
        self.root[char] = self.find(self.root[char])
        return self.root[char]
        
    def union(self, char1: string, char2: string):
        root1 = self.find(char1)
        root2 = self.find(char2)

        if root1 <= root2:
            self.root[root2] = root1
        else:
            self.root[root1] = root2

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        dSet = UnionFind()

        for i in range(len(s1)):
            dSet.union(s1[i], s2[i])
        
        smallestEqv = []

        for char in baseStr:
            smallestEqv.append(dSet.find(char))
        
        return ''.join(smallestEqv)

