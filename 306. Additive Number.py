class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        self.seq = []
        self.isAdditive = False 

        self.dfs(0, num)
        return self.isAdditive
        
    def dfs(self, indx, num):
        if indx >= len(num) and len(self.seq) > 2:
            self.isAdditive = True
        
        for i in range(indx, len(num)):
            currNum = num[indx: i + 1]
            # if the number has leadng zero
            if currNum[0] == '0' and len(currNum) > 1:
                return
            # if we have less than 2 elements in our list
            elif len(self.seq) < 2:
                self.seq.append(currNum)
                self.dfs(i + 1, num)
                self.seq.pop()
            # if the number meets the additive sequence rule
            elif int(currNum) == int(self.seq[-1]) + int(self.seq[-2]):
                self.seq.append(currNum)
                self.dfs(i + 1, num)
                self.seq.pop()
            # if currNum is less than the sum of preceding two elements in the list so we will skip this iteration for the current recursion
            elif int(currNum) < int(self.seq[-1]) + int(self.seq[-2]):
                continue
            # if currNum is greater than the sum of preceding two elements so we will sease this recursion 
            else:
                return 
            
