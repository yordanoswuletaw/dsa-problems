class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = defaultdict(lambda: 0)
        def dp(indx, sum):
            #base case
            if indx == len(nums):
                memo[(indx, sum)] = int(sum == target)
                return int(sum == target)
            if (indx, sum) in memo:
                return memo[(indx, sum)]
            
            #recurrence relation
            res = dp(indx + 1, sum - nums[indx]) + dp(indx + 1, sum + nums[indx])
            memo[(indx, sum)] = res 
            return res

        return dp(0, 0)
            
