class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        maxPiles = 0
        piles.sort()
        i, j = 0, len(piles) - 1
        while i < j:
            j -= 1
            maxPiles += piles[j]
            j -= 1
            i += 1
        return maxPiles
