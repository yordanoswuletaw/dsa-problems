class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)
        low, heigh = 1, max(piles)
        k = heigh

        while low <= heigh:
            mid = low + (heigh - low) // 2
            currHr = 0
            for pile in piles:
                currHr += ceil(pile / mid)
            if currHr <= h:
                k = min(k, mid)
                heigh = mid - 1
            else:
                low = mid + 1
        
        return k
        

