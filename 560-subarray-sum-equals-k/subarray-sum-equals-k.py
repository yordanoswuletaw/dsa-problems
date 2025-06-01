class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hash_map = {0: 1}
        running_sum = 0
        tot_subarrays = 0
        for num in nums:
            running_sum += num
            tot_subarrays += hash_map.get(running_sum - k, 0)
            hash_map[running_sum] = 1 + hash_map.get(running_sum, 0)
        
        return tot_subarrays

