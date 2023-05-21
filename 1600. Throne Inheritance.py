class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.famTree = defaultdict(list)
        self.dead = set()        

    def birth(self, parentName: str, childName: str) -> None:
        self.famTree[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        currOrder = []
        stack = [self.king]

        while stack:
            parent = stack.pop()
            if parent not in self.dead:
                currOrder.append(parent)
            for child in self.famTree[parent][::-1]:
                stack.append(child)
        
        return currOrder

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
