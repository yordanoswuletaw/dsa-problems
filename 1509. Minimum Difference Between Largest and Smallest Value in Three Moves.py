class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) <= 4:
            return 0

        nums.sort()
        ans1 = nums[-1] - nums[3]
        ans2 = nums[-4] - nums[0]
        ans3 = nums[-2] - nums[2]
        ans4 = nums[-3] - nums[1]

        return min(ans1, ans2, ans3, ans4)
