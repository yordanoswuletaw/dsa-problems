class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        # creating boustrophedon to indices converter
        board.reverse()
        def toIndices(sqr):
            row = (sqr - 1) // n
            col = (sqr - 1) % n
            if row % 2:
                col = n - col - 1
            return (row, col)
         
        queue = deque([(1, 0)])
        visited = set([1])
        # bfs 
        while queue:
            curr, moves = queue.popleft()
            start, end = curr + 1, min(curr + 6, n * n)
            for nxt in range(start, end + 1):
                row, col = toIndices(nxt)
                if board[row][col] != -1:
                    nxt = board[row][col]
                if nxt == n * n:
                    return moves + 1
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, moves + 1))

        return -1
