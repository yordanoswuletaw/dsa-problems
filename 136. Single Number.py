class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        singleNumber = 0

        for num in nums:
            singleNumber ^= num
        
        return singleNumber

       
