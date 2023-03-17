class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,heigh = 0, len(nums) - 1
        while low <= heigh:
            mid = (low + heigh) // 2
            if nums[mid] == target:
                return mid 
            elif target > nums[mid]:
                low = mid + 1
            else:
                heigh = mid - 1
        
        return low
        
