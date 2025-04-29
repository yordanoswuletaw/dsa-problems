class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        max_count = 0
        max_num = max(nums)
        start = 0
        ans = 0
        for end in range(n):
            if nums[end] == max_num:
                max_count += 1
            while start <= end and max_count >= k:
                ans += n - end
                if nums[start] == max_num:
                    max_count -= 1
                start += 1
        
        return ans
        