class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        triplets = set()
        for i in range(n - 2):
            hash_set = set()
            for j in range(i + 1, n):
                var = -nums[i] - nums[j]
                if var in hash_set:
                    triplets.add((nums[i], var, nums[j]))
                hash_set.add(nums[j])
        
        return [list(triplate) for triplate in triplets]
        