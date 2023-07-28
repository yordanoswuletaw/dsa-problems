class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        n, minNum = len(nums), nums[0]
        res, diffs = minNum, 0

        for i in range(1, n):
            diffs += nums[i] - minNum 
            if diffs > 0:
                res = max(res, minNum + ceil(diffs / (i + 1)))
        
        return res
