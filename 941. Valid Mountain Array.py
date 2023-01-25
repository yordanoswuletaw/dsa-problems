class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        n = len(arr)
        if n < 3:
            return False 
        
        i, j = 0, n - 1
        while i < j:
            if arr[i + 1] > arr[i]:
                 i += 1
            elif arr[j - 1] > arr[j]:
                j -= 1
            else:
                break 
        return i != 0 and j != n - 1 and i == j
