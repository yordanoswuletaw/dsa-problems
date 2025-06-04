class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        half = (n + m)//2
        left, right = 0, n - 1
        while True:
            med_index1 = left + (right - left) // 2
            med_index2 = half - med_index1 - 2

            left1 = nums1[med_index1] if med_index1 >= 0 else float('-inf')
            right1 = nums1[med_index1 + 1] if (med_index1 + 1) < n else float('inf')
            left2 = nums2[med_index2] if med_index2 >= 0 else float('-inf')
            right2 = nums2[med_index2 + 1] if (med_index2 + 1) < m else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                if (n + m) % 2:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = med_index1 - 1 
            else:
                left = med_index1 + 1
    
                