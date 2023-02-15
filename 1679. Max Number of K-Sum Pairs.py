class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        l, r = 0, len(nums) - 1
        ops = 0

        while l < r:
            currSum = nums[l] + nums[r]
            if k == currSum:
                ops += 1
                l += 1
                r -= 1 
            elif k < currSum:
                r -= 1
            else:
                l += 1
        
        return ops
