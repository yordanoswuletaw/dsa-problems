class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # using hashMap
        rows = {}
        output = 0
        for row in grid:
            rows[tuple(row)] = rows.get(tuple(row), 0) + 1
        
        for i in range(len(grid)):
            col = []
            for j in range(len(grid[0])):
                col.append(grid[j][i])
            output += rows.get(tuple(col), 0)
        
        return output
        
        # using matrix transpose
        # gridT = [[[] for i in range(len(grid))] for i in range(len(grid))]
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         gridT[j][i] = grid[i][j]
        
        # res = 0
        # for row in grid:
        #     for rowT in gridT:
        #         if row == rowT:
        #             res += 1
        

        # return res
