class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        start, end = 0, n - 1
        while start < end:
            for i in range(start, end):
                matrix[start][i], matrix[i][end], matrix[end][end-i+start], matrix[end-i+start][start] =  matrix[end-i+start][start], matrix[start][i], matrix[i][end], matrix[end][end-i+start]
            start += 1
            end -= 1