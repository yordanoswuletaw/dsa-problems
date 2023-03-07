class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0

        minLen, currSum = float('inf'), 0
        left = right = 0
        while right < len(nums):
            currSum += nums[right]
            right += 1

            while left <= right and currSum >= target:
                minLen = min(minLen, right - left)
                currSum -= nums[left]
                left += 1
                
            if minLen == 1:
                break
        
        return minLen
