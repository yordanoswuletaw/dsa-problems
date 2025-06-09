class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[-1] >= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        print(left)
        def bs(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        pivot = bs(0, left - 1)
        if pivot != -1:
            return pivot
        pivot = bs(left, n - 1)
        if pivot != -1:
            return pivot
        return -1