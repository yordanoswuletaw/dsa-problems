class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
    
        n = len(nums)
        prfx_sum = [0]
        for i in range(n):
            prfx_sum.append(prfx_sum[-1] + nums[i])

        start = 0
        ans = 0
        for end in range(1, n + 1):
            while start <= end and (prfx_sum[end] - prfx_sum[start]) * (end - start) >= k:
                start += 1
            
            ans += max(0, end - start)
        
        return ans

        