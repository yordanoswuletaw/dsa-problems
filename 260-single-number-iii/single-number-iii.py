class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        xor = 0
        for num in nums:
            xor ^= num
        
        diff = xor & (-xor)
        num1 = 0
        for num in nums:
            if num & diff:
                num1 ^= num
        
        return [num1, xor ^ num1]
        