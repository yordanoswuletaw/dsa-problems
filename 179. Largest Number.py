class LargestNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ''.join(sorted(map(str, nums), key=LargestNumKey))
        
        # using quick sort algorithm
    #     res = self.quickSort(nums)
    #     return '0' if res[0] == '0' else res
    
    # def quickSort(self, nums: List[int]) -> str:
    #     if len(nums) <= 1:
    #         return ''.join(map(str, nums))
        
    #     pivot = str(nums[0])
    #     left, right = [], []
    #     for num in nums[1:]:
    #         if str(num) + pivot > pivot + str(num):
    #             right.append(num)
    #         else:
    #             left.append(num)
    #     return self.quickSort(right) + pivot + self.quickSort(left)
