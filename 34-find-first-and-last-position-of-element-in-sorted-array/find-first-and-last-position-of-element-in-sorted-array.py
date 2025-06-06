class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        def bisect_left(left, right, target):
            indx = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        indx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return indx
        
        def bisect_right(left, right, target):
            indx = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        indx = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return indx

        return [bisect_left(0, n - 1, target), bisect_right(0, n - 1, target)]
        