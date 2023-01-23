class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        subBoxes = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                # skip empty cell
                if board[i][j] == '.':
                    continue
                # check for repetition in row, column and each 3 x 3 sub box
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in subBoxes[(i//3, j//3)]:
                    return False 
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                subBoxes[(i//3,j//3)].add(board[i][j])
      
        return True
