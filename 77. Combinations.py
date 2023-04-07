class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        self.combinations = []


        def dfs(comb, indx, k):
            if k <= 0:
                self.combinations.append(comb.copy())
                return
            
            for i in range(indx , n - k + 2):
                comb.append(i)
                dfs(comb, i + 1, k - 1)
                comb.pop()
        
        dfs([], 1, k)
        return self.combinations
        
