class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        max_triplate = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    max_triplate = max(max_triplate, (nums[i] - nums[j]) * nums[k])
        
        return max_triplate
        