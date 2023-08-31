class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return sum(nums)

        def dp(i, n, memo):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            res = max(nums[i] + dp(i + 2, n, memo), dp(i + 1, n, memo))
            memo[i] = res 
            return res
        
        return max(dp(0, len(nums) - 1, {}), dp(1, len(nums), {}))
