class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        secondMin, stack = float('inf'), []
        for num in nums:
            # check if there is a triplets
            if secondMin < num:
                return True
            # creating increasing monotonic stack
            while stack and stack[-1] >= num:
                stack.pop()
            #updating secondMin with the smallest mininum value
            stack.append(num)
            if len(stack) >= 2:
                secondMin = min(secondMin, stack[-1])
        
        return False
            
            
