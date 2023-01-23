class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        if len(grid) < 3 or len(grid[0]) < 3:
            return 0 
        
        output = 0

        for row_end in range(2, len(grid)):
            # compute sum of the first 3 x 3 grid
            for col_end in range(2, len(grid[0])):
                row, col = row_end - 2, col_end - 2
                if self.checkMagicSquare(grid, row, col, row_end, col_end):
                    output += 1

        return output
    
    def checkMagicSquare(self, grid, row, col, row_end, col_end):
        hashMap = {}
        row_sum = [0] * 3
        col_sum = [0] * 3
        diag1_sum = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]
        diag2_sum = grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col]

        # sum each row and column
        for i in range(row, row_end + 1):
            for j in range(col, col_end + 1):
                if grid[i][j] < 1 or grid[i][j] > 9 or grid[i][j] in hashMap:
                    return False 
                row_sum[i - row] += grid[i][j]
                col_sum[j - col] += grid[i][j]
            
                hashMap[grid[i][j]] = True 

        # check magic square
        if len(set(row_sum)) == len(set(col_sum)) == 1:
            if row_sum[0] == col_sum[0] == diag1_sum == diag2_sum:
                return True 
                
        return False

                


        
