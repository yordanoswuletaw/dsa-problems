class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        maxNum = 0

        i = j = 0
        while j < len(nums):
            # traversing seeker pointer
            if nums[j]:
                j += 1
            elif k > 0:
                j += 1
                k -= 1
            # updating placeholder and k
            else:
                maxNum = max(maxNum, j - i)
                if not nums[i]:
                    k += 1
                i += 1
        maxNum = max(maxNum, j - i)
        return maxNum
