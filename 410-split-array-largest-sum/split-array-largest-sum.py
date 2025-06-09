class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        n = len(nums)
        left, right = min(nums), sum(nums)
        while left <= right:
            target_sum = left + (right - left) // 2
            split = 1
            subarray_sum = 0
            for i in range(n):
                if subarray_sum + nums[i] > target_sum:
                    split += 1
                    subarray_sum = 0
                subarray_sum += nums[i]

            if split <= k:
                right = target_sum - 1
            else:
                left = target_sum + 1
        max_target_sum = subarray_sum = 0
        for i in range(n):
                if subarray_sum + nums[i] > left:
                    max_target_sum = max(max_target_sum, subarray_sum)
                    subarray_sum = 0
                subarray_sum += nums[i]
        return max(max_target_sum, subarray_sum)
