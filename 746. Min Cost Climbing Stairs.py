class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}

        def dp(n):
            nonlocal cost
            if n >= len(cost):
                return 0
            
            if n in memo:
                return memo[n]
            
            currCost = cost[n] + min(dp(n + 1), dp(n + 2))
            memo[n] = currCost

            return currCost
        
        dp(0)
        return min(memo[0], memo[1])
