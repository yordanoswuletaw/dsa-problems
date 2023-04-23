class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        n = len(cookies)
        self.result = sum(cookies)

        def dfs(indx, childs, currMax):
            
            if indx == n:
                self.result = min(self.result, currMax)
                return
            
            for i in range(0, min(indx +1, k)):
                childs[i] += cookies[indx]
                dfs(indx + 1, childs, max(childs[i], currMax))
                childs[i] -= cookies[indx]
        
        dfs(0, [0] * k, 0)
        
        return self.result
        

        
