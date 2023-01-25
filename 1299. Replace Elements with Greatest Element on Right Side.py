class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        currMax = -1
        
        # replacing the array with the current max starting from right to left
        for i in range(len(arr)-1, -1, -1):
            currMax, arr[i] = max(arr[i], currMax), currMax
        return arr
