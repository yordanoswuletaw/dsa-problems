class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        loner = 0
        for shift_bit in range(32):
            loner_bit = 0
            for num in nums:
                loner_bit += ((num >> shift_bit) & 1)
        
            loner_bit %= 3
            loner = loner | (loner_bit << shift_bit)
        
        if loner >= (1 << 31):
            return loner - (1 << 32)
        
        return loner