class UnionFind:

    def __init__(self):
        self.root = {char: char for char in string.ascii_lowercase}
        self.rank = [1] * 26
    
    def find(self, char: string):
        if char == self.root[char]:
            return char
        self.root[char] = self.find(self.root[char])
        return self.root[char]
    
    def union(self, char1: string, char2: string):
        root1 = self.find(char1)
        root2 = self.find(char2)

        num1, num2 = ord(root1) % 97, ord(root2) % 97
        if self.rank[num1] < self.rank[num2]:
            self.root[root1] = root2
            self.rank[num2] += self.rank[num1]
        else:
            self.root[root2] = root1
            self.rank[num1] += self.rank[num2]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        equalSet = UnionFind()
        for eq in equations:
            opd1, opr, opd2 = eq[0], eq[1:3], eq[3]
            if opr == '==':
                equalSet.union(opd1, opd2)
            
        for eq in equations:
            opd1, ops , opd2 = eq[0], eq[1:3], eq[3] 
            if ops == '!='and equalSet.find(opd1) == equalSet.find(opd2):
                return False
            
        return True
