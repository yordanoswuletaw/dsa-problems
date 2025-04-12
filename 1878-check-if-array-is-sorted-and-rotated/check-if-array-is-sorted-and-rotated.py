class Solution:
    def check(self, nums: List[int]) -> bool:

        indx = 1
        while indx < len(nums) and nums[indx] >= nums[indx - 1]:
            indx += 1
        
        left = float('-inf')
        right = nums[0]
        while indx < len(nums) and left <= nums[indx] <= right:
            left = nums[indx]
            indx += 1
        
        return indx >= len(nums)
        