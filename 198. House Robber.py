class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        def dp(n):
            if n >= len(nums):
                return 0
            if n in memo:
                return memo[n]
            
            result = max(nums[n] + dp(n + 2), dp(n + 1))
            memo[n] = result
            return result
        
        return dp(0)

        # iterative solution
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2 
            rob2 = temp
        return temp
