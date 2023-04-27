class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
    
        puzzles = []
        chessboard = [['.' for i in range(n)] for i in range(n)]
        # hashSet to record veirtical attack reginons
        vSet = set()
          # hashSet to record diagonal attack reginons
        diagSet = set()
          # hashSet to record reverse diagonal attack reginons
        revDiagSet = set()

        def solve(row):
            if row >= n:
                cpyBoard = ["".join(each) for each in chessboard]
                puzzles.append(cpyBoard)
                return
            
            for col in range(n):
                # if i,j in any of the hashSet we will skip the current inner-loop iteration
                if col in vSet or row - col in diagSet or col + row in revDiagSet:
                    continue
                
                chessboard[row][col] = 'Q'
                vSet.add(col)
                diagSet.add(row - col)
                revDiagSet.add(row + col)

                # if valid position found for the current row then we will look for next valid position until we found n positions
                solve(row + 1)

                chessboard[row][col] = '.'
                vSet.remove(col)
                diagSet.remove(row - col)
                revDiagSet.remove(row + col)
            
        
        solve(0)

        return puzzles
