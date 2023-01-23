class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowSet = {}
        colSet = {}

        def validateSudoku(rowStart, rowEnd, colStart, colEnd):

            # hashSet to check for repetition in 3x3 matrix
            hashSet = set()
            for i in range(rowStart, rowEnd):
                for j in range(colStart, colEnd):

                    if board[i][j] != '.':
                        # if digit is between 1 - 9 and unique
                        if int(board[i][j]) < 0 or int(board[i][j]) > 9 or board[i][j] in hashSet:
                            return False 
                        hashSet.add(board[i][j])
                    
                        # check if digits in row are unique
                        if i in rowSet:  
                            if board[i][j] in rowSet[i]:
                                return False
                            rowSet[i].add(board[i][j]) 
                        else:
                            rowSet[i] = set(board[i][j])
                        
                        # check if digits in column are unique
                        if j in colSet:
                            if board[i][j] in colSet[j]:
                                return False
                            colSet[j].add(board[i][j]) 
                        else:
                            colSet[j] = set(board[i][j])
                        
                        
            return True
        
        for i in range(2, 9, 3):
            for j in range(2, 9, 3):
                if not validateSudoku(i - 2, i + 1, j - 2, j + 1):
                    return False
      
        return True
