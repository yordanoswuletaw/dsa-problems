class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        numTable = {}
        for i in range(len(nums)):
            numTable[nums[i]] = i 
        
        for op in operations:
            nums[numTable[op[0]]] = op[1]
            numTable[op[1]] = numTable[op[0]]
        
        return nums
