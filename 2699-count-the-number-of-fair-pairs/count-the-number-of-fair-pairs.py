class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums.sort()

        fair_pairs = 0
        for i, num in enumerate(nums):
            left_indx = bisect.bisect_left(nums, lower - num)
            left_indx = max(left_indx, i + 1)

            right_indx = bisect.bisect_right(nums, upper - num)
            right_indx = max(right_indx, i + 1)

            fair_pairs += right_indx - left_indx
        
        return fair_pairs
        