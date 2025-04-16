class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        n = len(nums)
        start = 0
        hashmap = defaultdict(int)
        k_count = ans = 0
        for end in range(n):
            prev_pairs = hashmap[nums[end]] * (hashmap[nums[end]] - 1)//2
            k_count -= prev_pairs
            hashmap[nums[end]] += 1
            pairs = hashmap[nums[end]] * (hashmap[nums[end]] - 1)//2
            k_count += pairs
            
            while  k_count >= k:
                ans += n - end
                k_count -= hashmap[nums[start]] - 1
                hashmap[nums[start]] -= 1
                start += 1

        return ans 