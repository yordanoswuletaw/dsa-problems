class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        indx, last_num = self.hashmap[val], self.arr[-1]
        self.arr[indx], self.hashmap[last_num] = last_num, indx
        del self.hashmap[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()