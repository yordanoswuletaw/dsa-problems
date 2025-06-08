class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 1:
            return 0
        jumps = 1
        prev_jump = nums[0]
        next_jump = 0
        for i in range(1, n):
            if prev_jump >= i:
                next_jump = max(next_jump, i + nums[i])
            else:
                jumps += 1
                prev_jump = next_jump
                next_jump = max(next_jump, i + nums[i])
        
        return jumps

       