class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        n, m = len(matrix), len(matrix[0])
        # inserting zero value array 
        self.matrix = [[0 for i in range(m)]] + matrix
        for i in range(n + 1):
            self.matrix[i].insert(0,0)
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.matrix[i][j] += self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1] + self.matrix[row1][col1]
       
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
