class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        i, j = 0, 1
        while j < len(nums):
            # since the sumation of 2 greater numbers does not result a smaller number
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2
        return nums
