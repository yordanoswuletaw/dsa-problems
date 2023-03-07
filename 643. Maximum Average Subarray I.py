class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        i = j = 0
        sum, maxAverage, size = 0, float('-inf'), k
        while j < len(nums):
            if k > 0:
                sum += nums[j]
                k -= 1
            else:
                maxAverage = max(maxAverage, sum / size)
                sum -= nums[i]
                sum += nums[j]
                i += 1
            j += 1

        return max(maxAverage, sum / size)
