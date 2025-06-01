class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reverse_array(start, end, arr):
            while start <= end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            
        reverse_array(0, n - 1, nums)
        reverse_array(0, k - 1, nums)
        reverse_array(k, n - 1, nums)

        