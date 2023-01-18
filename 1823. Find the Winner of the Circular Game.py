class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        players = list(range(1, n+1))
        k = k - 1
        pointer = 0
        while n > 1:
            pointer = (pointer + k) % n 
            players.pop(pointer)
            n -= 1 
        return players[0]

