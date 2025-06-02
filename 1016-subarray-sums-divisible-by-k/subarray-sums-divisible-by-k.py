class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        hash_map = {0: 1}
        tot_subarrays = 0
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            tot_subarrays += hash_map.get(running_sum % k,0)
            hash_map[running_sum % k] = 1 + hash_map.get(running_sum % k, 0)
        
        return tot_subarrays