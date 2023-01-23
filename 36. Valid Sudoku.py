class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowTable = {}
        colTable = {}

        def validateSudoku(rowStart, rowEnd, colStart, colEnd):

            hashMap = {}
            for i in range(rowStart, rowEnd):
                for j in range(colStart, colEnd):
                    if board[i][j] != '.':
                        if int(board[i][j]) < 0 or int(board[i][j]) > 9 or board[i][j] in hashMap:
                            return False 
                        hashMap[board[i][j]] = 1
                        if i in rowTable:
                            rowTable[i].append(board[i][j]) 
                        else:
                            rowTable[i] = list([board[i][j]])
                        if j in colTable:
                            colTable[j].append(board[i][j]) 
                        else:
                            colTable[j] = list([board[i][j]])
                        
            return True
        
        for i in range(2, 9, 3):
            for j in range(2, 9, 3):
                if not validateSudoku(i - 2, i + 1, j - 2, j + 1):
                    return False
        for i in range(9):
            if i in rowTable:
                if len(rowTable[i]) != len(set(rowTable[i])):
                    return False
            if i in colTable:
                 if len(colTable[i]) != len(set(colTable[i])):
                    return False
        return True
