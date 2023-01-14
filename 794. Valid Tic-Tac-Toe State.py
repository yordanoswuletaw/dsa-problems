from collections import Counter
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        moves = {}
        
        for row in range(3):
           for col in range(3):
                moves[board[row][col]] = moves.get(board[row][col], 0) + 1
       
        # check X and O points
        if moves.get('X', 0) < moves.get('O', 0) or moves.get('X', 0) - moves.get('O', 0) > 1:
            return False
        
        X_won = self.checkWinStatus(board, 'X')
        O_won = self.checkWinStatus(board, 'O')

        # if both team winns
        if X_won and O_won:
            return False

        # if Player with X symoble winns
        if X_won and moves.get('X', 0) <= moves.get('O', 0):
            return False
        
        # if Player with X symoble winns
        if O_won and moves.get('X', 0) > moves.get('O', 0):
            return False
                
        return True

    def checkWinStatus(self, board, player):

        # check row status
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True 
        
        #check column status
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True 
        
        #check diagonal Status
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True

        return False
