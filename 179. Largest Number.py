class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = self.quickSort(nums)
        return '0' if res[0] == '0' else res
    
    def quickSort(self, nums: List[int]) -> str:
        if len(nums) <= 1:
            return ''.join(map(str, nums))
        
        pivot = str(nums[0])
        left, right = [], []
        for num in nums[1:]:
            if str(num) + pivot > pivot + str(num):
                right.append(num)
            else:
                left.append(num)
        return self.quickSort(right) + pivot + self.quickSort(left)
