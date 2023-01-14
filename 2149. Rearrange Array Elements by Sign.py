class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        output = [0] * len(nums)
        ntv, ptv = 1, 0
        for num in nums:
            if num > 0:
               output[ptv] = num
               ptv += 2
            else:
                output[ntv] = num
                ntv += 2
        
        return output

        # optimization using two pointers
        # i, j = 0, 1
        # while j < len(nums):
        #     if nums[i] > 0 and nums[j] < 0:
        #         i += 2
        #         j += 2

        #     elif nums[i] < 0 and nums[j] > 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 2
        #         j += 2

        #     elif nums[i] > 0 and nums[j] > 0:
        #         k = j
        #         while j < len(nums) and nums[j] > 0:
        #             j += 1
        #         while j < len(nums) and k+1 != j and nums[k] > 0 and nums[j] < 0:
        #             nums[k+1], nums[j] = nums[j], nums[k+1]
        #             k += 2
        #             j += 1
        #         i = k
        #         j = i + 1

        #     elif nums[i] < 0 and nums[j] < 0:
        #         k = i
        #         while i < len(nums) and nums[i] < 0:
        #             i += 1
        #         while i < len(nums) and k+1 != i and nums[k] < 0 and nums[i] > 0:
        #             nums[k], nums[k+1] = nums[k+1], nums[k]
        #             nums[k], nums[i] = nums[i], nums[k]
        #             k += 2
        #             i += 1
        #         j = k + 1
        #         i = j - 1
        # return nums
                
