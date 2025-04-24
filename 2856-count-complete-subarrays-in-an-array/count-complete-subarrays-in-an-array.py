class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        unique_elements = set(nums)
        curr_unique = defaultdict(int)
        left = 0
        ans = 0
        n = len(nums)
        for right in range(n):
            curr_unique[nums[right]] += 1
            while set(curr_unique.keys()) == unique_elements:
                ans += (n - right)
                curr_unique[nums[left]] -= 1
                if curr_unique[nums[left]] == 0:
                    curr_unique.pop(nums[left])
                left += 1
        
        return ans
        