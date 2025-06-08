class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        permutations = []
        def backtrack(nums, permutation):
            if not nums:
                permutations.append(permutation[::])
                return 
            
            for i in range(len(nums)):
                permutation.append(nums[i])
                backtrack(nums[:i] + nums[i+1:], permutation)
                permutation.pop()
        
        backtrack(nums, [])
        return permutations

