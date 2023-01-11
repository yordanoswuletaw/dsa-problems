class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            # store nums[i] as remainder and nums[nums[i]] as quotient
            nums[i] = nums[i] + (nums[nums[i]] % 1024) * 1024
        
        # store quotients only in nums
        for i in range(len(nums)):
            nums[i] //= 1024
           
        return nums
