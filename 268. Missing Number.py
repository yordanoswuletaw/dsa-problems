class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # actualSum, currSum = 0, 0
        # for i in range(len(nums)):
        #     actualSum += i + 1
        #     currSum += nums[i]
        # return actualSum - currSum

        ln = len(nums)
        for indx in range(len(nums)):
            ln += indx - nums[indx]
        return ln
        
