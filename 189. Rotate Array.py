class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        # using two pointer technique
        nums.reverse()
        l, r = 0, k - 1
        # reverse the first k elements
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l, r = k, n - 1
        # reverse the last n - k elements
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        # pythonic
        # nums[:] = nums[n - k:] + nums[:n - k]
                
