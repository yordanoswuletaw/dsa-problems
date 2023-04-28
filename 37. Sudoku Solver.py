class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.found = False
        rows = defaultdict(set)
        cols = defaultdict(set)
        subBoard = defaultdict(set)
        
        # adding each digit in row, column and sub-boxes hashset
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    subBoard[(i //3, j //3)].add(board[i][j])
        

        def solve(row, col):
            # validation or base case
            row = row + col // 9
            col = col % 9

            if row > 8:
                self.found =  True
                return 

            for j in range(col, 9):
                if board[row][j] == '.':
                    for val in map(str, range(1, 10)):
                        if val not in rows[row] and val not in cols[j] and val not in subBoard[(row//3, j//3)]:
                            board[row][j] = val
                            rows[row].add(val)
                            cols[j].add(val)
                            subBoard[(row//3, j//3)].add(val)
                    
                            solve(row, j + 1)

                            if not self.found:
                                board[row][j] = '.'
                                rows[row].remove(val)
                                cols[j].remove(val)
                                subBoard[(row//3,j//3)].remove(val)

                    # if no valid digit found    
                    if board[row][j] == '.':
                        return
                        
            # to move to the next row after completing the current row
            if not self.found:
                solve(row, 9) 

        solve(0,0)
            

        
       
