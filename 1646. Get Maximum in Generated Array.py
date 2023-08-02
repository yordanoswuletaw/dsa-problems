class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        if n <= 1:
            return n

        n += 1
        nums = [0] * n
        nums[1] = 1

        for i in range(n // 2):
            if i * 2 < n:
                nums[i * 2] = max(nums[i * 2], nums[i])
            if i * 2 + 1 < n:
                nums[i * 2 + 1] = max(nums[i * 2 + 1], nums[i] + nums[i + 1])
        
        return max(nums)
