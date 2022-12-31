class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''
        for any triangle to form a triangle with non-zero area lets say side a, b, c the following condition
        should be satisfied: a <= b <= c and a+b > c
        '''
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
