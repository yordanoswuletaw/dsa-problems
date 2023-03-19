class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        low, heigh = 0, len(arr) - 1

        while low <= heigh:
            mid = low + (heigh - low) // 2
            if 0 < mid < len(arr) - 1 and arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid 
            elif 0 < mid and arr[mid - 1] >= arr[mid]:
                heigh = mid - 1
            elif len(arr) - 1 > mid and arr[mid + 1] >= arr[mid]:
                low = mid + 1

        return mid 
