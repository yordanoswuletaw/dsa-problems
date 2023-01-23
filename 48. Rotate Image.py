class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # start and end used as a boundery to traverse the array from outside in
        start, end = 0, len(matrix) - 1
        while start < end:
            for i in range(start, end):
                # rotating cells
                matrix[start][i], matrix[i][end], matrix[end][end - i + start], matrix[end - i + start][start] = matrix[end - i + start][start], matrix[start][i], matrix[i][end], matrix[end][end - i + start]

            start += 1
            end -= 1
