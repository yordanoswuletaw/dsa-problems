class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        # apply operations
        ptr1, ptr2 = 0, 1
        while ptr2 < len(nums):
            if nums[ptr1] != 0 and nums[ptr2]!= 0:
                if nums[ptr1] == nums[ptr2]:
                    nums[ptr1] *= 2
                    nums[ptr2] = 0
                    ptr1 += 1
                    ptr2 += 1
            ptr1 += 1
            ptr2 += 1
        
        # move zeros
        ptr1, ptr2 = 0, 1
        while ptr2 < len(nums):
            if nums[ptr1] != 0 or (nums[ptr1] == 0 and nums[ptr2] != 0):
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1
            ptr2 += 1

        return nums
            
