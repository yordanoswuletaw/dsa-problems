class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        target = sum(nums) % p
        if target == 0:
            return 0
        hashmap = {0: -1}
        subarray_len = len(nums)
        running_sum = 0
        for i in range(len(nums)):
            running_sum = (running_sum + nums[i]) % p
            needed = (running_sum - target + p) % p 
            if needed in hashmap:
                subarray_len = min(subarray_len, i - hashmap[needed])
            hashmap[running_sum] = i
        
        return subarray_len if subarray_len < len(nums) else -1