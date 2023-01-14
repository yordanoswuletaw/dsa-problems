class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

         tRow, bRow = 0, len(matrix) - 1
         lCol, rCol = 0, len(matrix[0]) - 1
         output = []
         i = j = 0

         while tRow <= bRow and lCol <= rCol:
             # traversing from left to right
            if i == tRow and j == lCol:
                while j <= rCol:
                     output.append(matrix[i][j]) 
                     j += 1
                j -= 1
                i += 1
                tRow += 1
            # traversing from upward to downward
            elif i == tRow and j == rCol:
                while i <= bRow:
                    output.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                rCol -= 1
            # traversing from right to left
            elif i == bRow and j == rCol:
                while j >= lCol:
                    output.append(matrix[i][j])
                    j -= 1
                j += 1
                i -= 1
                bRow -= 1
            # traversing from down to upward
            elif i == bRow and j == lCol:
                while i >= tRow:
                    output.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                lCol += 1

         return output
            




