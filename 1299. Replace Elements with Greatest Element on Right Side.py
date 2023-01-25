class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        currMax = arr[-1]
        arr[-1] = -1
        
        # replacing the array with the current max starting from right to left
        for i in range(len(arr)-2, -1, -1):
            currMax, arr[i] = max(arr[i], currMax), currMax
        return arr
