class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dp(indx, curr_sum):
            if indx == len(coins) or curr_sum > amount:
                return float('inf')
            if amount == curr_sum:
                return 0
            if (indx, curr_sum) in memo:
                return memo[(indx, curr_sum)]
            
            memo[(indx, curr_sum)] = min(1 + dp(indx, curr_sum + coins[indx]), dp(indx + 1, curr_sum))
            return memo[(indx, curr_sum)]
        
        ans = dp(0, 0)
        if ans == float('inf'):
            return -1
        return ans


            
            