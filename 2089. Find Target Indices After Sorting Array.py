class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()
        i, j = 0, len(nums) - 1
        start = end = 0
        while i <= j:
            mid = (i + j) // 2
            # finding the target index
            if nums[mid] == target:
                 start = end = mid
                 # scanning left for the target
                 while start >= 0 and nums[start] == target:
                     start -= 1
                 # scaning right for the target
                 while end < len(nums) and nums[end] == target:
                     end += 1
                 return list(range(start + 1, end))
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return []
