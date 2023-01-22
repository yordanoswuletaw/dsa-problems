class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left, right, = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        output = []

        while left <= right and top <= bottom:

            # traversing from left to right
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1

            # traversing from top to bottom
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1

            # check if we can traverse back to left or top
            if left > right or top > bottom:
                break 
            # traverse back to left
            for i in range(right, left - 1, -1):
                output.append(matrix[bottom][i])
            bottom -= 1

            # traversing back to top
            for i in range(bottom, top - 1, -1):
                output.append(matrix[i][left])
            left += 1

        return output

        #  tRow, bRow = 0, len(matrix) - 1
        #  lCol, rCol = 0, len(matrix[0]) - 1
        #  output = []
        #  i = j = 0

        #  while tRow <= bRow and lCol <= rCol:
        #      # traversing from left to right
        #     if i == tRow and j == lCol:
        #         while j <= rCol:
        #              output.append(matrix[i][j]) 
        #              j += 1
        #         j -= 1
        #         i += 1
        #         tRow += 1
        #     # traversing from upward to downward
        #     elif i == tRow and j == rCol:
        #         while i <= bRow:
        #             output.append(matrix[i][j])
        #             i += 1
        #         i -= 1
        #         j -= 1
        #         rCol -= 1
        #     # traversing from right to left
        #     elif i == bRow and j == rCol:
        #         while j >= lCol:
        #             output.append(matrix[i][j])
        #             j -= 1
        #         j += 1
        #         i -= 1
        #         bRow -= 1
        #     # traversing from down to upward
        #     elif i == bRow and j == lCol:
        #         while i >= tRow:
        #             output.append(matrix[i][j])
        #             i -= 1
        #         i += 1
        #         j += 1
        #         lCol += 1
        # return output
