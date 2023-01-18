class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n, m =  len(matrix),  len(matrix[0])
        leftPtr, rightPtr = 0, n * m - 1
        while leftPtr <= rightPtr:
            midPtr = (leftPtr + rightPtr) // 2
            if matrix[midPtr // m][midPtr % m] == target:
                return True 
            elif matrix[midPtr // m][midPtr % m] < target:
                leftPtr = midPtr + 1
            else:
                rightPtr = midPtr - 1

        return False
        
        # l, r = 0, len(matrix) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if l == r:
        #         l2, r2 = 0, len(matrix[l]) - 1 
        #         while l2 <= r2:
        #             mid = (l2 + r2) // 2
        #             if matrix[l][mid] == target:
        #                 return True 
        #             elif matrix[l][mid] > target:
        #                 r2 = mid - 1
        #             else:
        #                 l2 = mid + 1
        #     if matrix[mid][0] == target:
        #         return True 
        #     elif matrix[mid][0] > target:
        #         r = mid - 1
        #     elif matrix[mid][len(matrix[mid])-1] == target:
        #         return True
        #     elif matrix[mid][len(matrix[mid])-1] < target:
        #         l = mid + 1
        #     else:
        #         l = r = mid
        #         break
        # return False       
