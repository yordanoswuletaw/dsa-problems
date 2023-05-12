class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxOR = 0
        self.res = 0
        nums.sort(reverse=True)

        for num in nums:
            maxOR |= num 

        def backtrack(indx, currOR):
            if indx >= len(nums):
                return 
            
            for i in range(indx, len(nums)):
                if currOR | nums[i] == maxOR:
                    self.res += 1 + (2 ** (len(nums) - i - 1) - 1)
                    continue
                backtrack(i + 1, currOR | nums[i])
        
        backtrack(0, 0)
        return self.res
