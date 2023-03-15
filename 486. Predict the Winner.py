class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def predict(left, right):
            if left == right:
                return nums[left]

            leftOption = nums[left] - predict(left + 1, right)
            rightOption = nums[right] - predict(left, right - 1)

            return max(leftOption, rightOption)
            
        return predict(0, len(nums) - 1) >= 0
