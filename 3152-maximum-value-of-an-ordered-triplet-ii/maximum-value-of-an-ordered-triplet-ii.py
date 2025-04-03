class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        n = len(nums)
        hashmap = defaultdict(list)
        left_max = nums[0]
        for i in range(1, n - 1):
            hashmap[i].append(left_max)
            left_max = max(left_max, nums[i])
        
        right_max = nums[-1]
        for i in range(n - 2, 0, -1):
            hashmap[i].append(right_max)
            right_max = max(right_max, nums[i])
       
        max_triplets = 0
        for index, (left_max, right_max) in hashmap.items():
            max_triplets = max(max_triplets, (left_max - nums[index]) * right_max)
        
        return max_triplets



        
        