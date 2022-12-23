class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxSum = 0
        for i in range(len(grid)):
            #break the loop if the remain matrix can't make hourglass
            if(i + 3) > len(grid):
                break
            # initially calculate the first sum of the hourglass
            currMax = currSum = sum(grid[i][:3]) + sum(grid[i+2][:3]) + grid[i+1][1]
            for j in range(3,len(grid[0])):
                # increase the column by 1 and re compute hourglass sum
                currSum = currSum + grid[i][j] + grid[i+2][j] + grid[i+1][j-1] - grid[i+1][j-2]- grid[i+2][j-3] - grid[i][j-3]
                # take the maximum sum for the columns
                currMax = max(currMax, currSum)
            maxSum = max(maxSum, currMax)
        return maxSum
            
