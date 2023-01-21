class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        # brute force
        output = []

        rowEnd = 2
        # traverse every 3 row sections
        while rowEnd < len(grid):
            currRow = []
            colEnd = 2
            
            # traverse every 3 column sections
            while colEnd < len(grid[0]):
                currMax = 0
                rowStart = rowEnd - 2

                #find the maximum value in 3 by 3 grid
                while rowStart <= rowEnd:
                    colStart = colEnd - 2
                    while colStart <= colEnd:
                        currMax = max(currMax, grid[rowStart][colStart])
                        colStart += 1
                    rowStart += 1
                colEnd += 1

                # append the first max values in to output
                currRow.append(currMax)
            rowEnd += 1
            output.append(currRow)

        return output
