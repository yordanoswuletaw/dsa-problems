class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * (max(nums) + 1)
        for num in nums:
            count[num] += 1
        
        target = 0
        for i,c in enumerate(count):
            nums[target:target + c] = [i] * c
            target += c
    
        return nums
