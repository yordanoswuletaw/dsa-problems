class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        tot_sum = sum(nums)
        if tot_sum % 2:
            return False
        half_sum = tot_sum // 2

        def dp(indx, half_sum):
            if half_sum == 0:
                return True
            if indx == len(nums):
                return False
            
            if (indx, half_sum) in memo:
                return memo[(indx, half_sum)]
            
            memo[(indx, half_sum)] = dp(indx + 1, half_sum - nums[indx]) or dp(indx + 1, half_sum)
            return memo[(indx, half_sum)]
        
        memo = {}
        return dp(0, half_sum)
        