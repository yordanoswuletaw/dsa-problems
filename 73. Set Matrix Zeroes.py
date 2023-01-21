class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1) space
        n, m = len(matrix), len(matrix[0])
        is_col_zero = False
        for row in range(n):
            if matrix[row][0] == 0:
                is_col_zero = True
            for col in range(1, m):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1, n):
            for col in range(1, m):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for col in range(m):
                matrix[0][col] = 0
        
        if is_col_zero:
            for row in range(n):
                matrix[row][0] = 0
                

        # O(nm) space
        # zerosRow = set()
        # zerosCol = set()

        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         if matrix[row][col] == 0:
        #             zerosRow.add(row)
        #             zerosCol.add(col)
        
        # for row in tuple(zerosRow):
        #     matrix[row] = [0] * len(matrix[0])
        
        # for col in tuple(zerosCol):
        #     for row in range(len(matrix)):
        #         matrix[row][col] = 0
        
