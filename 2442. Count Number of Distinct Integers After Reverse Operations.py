class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        hashSet = set()

        for i in range(len(nums)):
            hashSet.add(nums[i])
            if nums[i] > 9:
                hashSet.add(self.reverse(nums[i]))
        
        return len(hashSet)
        
    def reverse(self, num):
        res = 0
        while num:
            res *= 10
            res += (num % 10)
            num = num // 10
        return res
