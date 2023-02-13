class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        indx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[indx] = nums[i]
                indx += 1
        return indx 
