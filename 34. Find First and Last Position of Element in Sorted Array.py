class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        res, n = [-1, -1], len(nums)
        # finding the starting position
        low, heigh = 0, n - 1
        while low <= heigh:
            mid = low + (heigh - low) // 2
            if nums[mid] == target:
                res[0] = mid 
                heigh = mid - 1
            elif nums[mid] > target:
                heigh = mid - 1
            else:
                low = mid + 1
        
        # finding the ending position
        low, heigh = 0, n - 1
        while low <= heigh:
            mid = low + (heigh - low) // 2
            if nums[mid] == target:
                res[1] = mid 
                low = mid + 1
            elif nums[mid] > target:
                heigh = mid - 1
            else:
                low = mid + 1
        
        return res

        # using recursion
        # res = [-1, -1]
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         left = self.searchRange(nums[l:mid], target)
        #         right = self.searchRange(nums[mid+1:r+1], target)
        #         res[0] = min(mid, l + left[0]) if left[0] != -1 else mid
        #         res[1] = max(mid, mid + 1 + right[1]) if right[1] != -1 else mid
        #         break
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        
        # return res

