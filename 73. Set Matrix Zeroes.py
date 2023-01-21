class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerosRow = set()
        zerosCol = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zerosRow.add(row)
                    zerosCol.add(col)
        
        for row in tuple(zerosRow):
            matrix[row] = [0] * len(matrix[0])
        
        for col in tuple(zerosCol):
            for row in range(len(matrix)):
                matrix[row][col] = 0
        
