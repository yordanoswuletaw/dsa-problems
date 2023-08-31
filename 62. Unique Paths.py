class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dp(i, j, memo):
            nonlocal m, n
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = dp(i + 1, j, memo)
            res += dp(i, j + 1, memo)
            memo[(i, j)] = res

            return res
        
        return dp(0, 0, {})

        
