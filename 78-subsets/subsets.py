class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        all_possible_subsets = [[]]
        def backtracking(indx, subset):
            if indx == len(nums):
                return
            for i in range(indx, len(nums)):
                subset.append(nums[i])
                all_possible_subsets.append(subset.copy())
                backtracking(i + 1, subset)
                subset.pop()
        
        backtracking(0, [])
        return all_possible_subsets