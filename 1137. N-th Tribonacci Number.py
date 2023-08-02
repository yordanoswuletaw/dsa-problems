class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def tribonacci(n):
            if n == 0:
                return 0
            if n <= 2:
                return 1
            if n in memo:
                return memo[n]
            
            result = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
            memo[n] = result
            return result
        
        return tribonacci(n)
        
