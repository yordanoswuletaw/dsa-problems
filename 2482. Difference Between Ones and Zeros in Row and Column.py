class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        output = [[] for i in range(len(grid))]
        
        rowSum, colSum = [0] * len(grid), [0] * len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rowSum[i] += grid[i][j]
                colSum[j] += grid[i][j]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rowDiff = rowSum[i] - (len(grid[0]) - rowSum[i])
                colDiff = colSum[j] - (len(grid) - colSum[j])
                output[i].append( rowDiff + colDiff)

        return output
