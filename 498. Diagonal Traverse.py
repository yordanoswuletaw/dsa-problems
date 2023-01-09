class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        n, m = len(mat), len(mat[0])
        output = []
        direction = 1
        row = col = 0

        for _ in range(n * m):
            # tuning row 
            # if row less than zero or column grater than m   
            if row < 0 or col >= m:
                if col >= m:
                    col = m - 1
                    row += 1
                row += 1
                direction -= 1

            # tuning column
            # if column less than zero or row grater than n
            if col < 0 or row >= n:
                if row >= n:
                    row = n - 1
                    col += 1
                col += 1
                direction += 1 

            output.append(mat[row][col])

            # traversing upward
            if direction:
                row -= 1
                col += 1
            # traversing downward
            else:
                row += 1
                col -= 1

        return output
            
            
