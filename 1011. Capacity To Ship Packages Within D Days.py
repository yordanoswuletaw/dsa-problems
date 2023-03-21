class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low, heigh = max(weights), sum(weights)
        leastWeight = heigh

        while low <= heigh:
            # capacity
            mid = low + (heigh - low) // 2

            # calculate the day it takes for the capacity 'mid'
            currWeight, currDays = 0, 1
            for weight in weights:
                if currWeight + weight > mid:
                    currWeight = 0
                    currDays += 1
                currWeight += weight
            
            # deciding either to minmize or maximize the capacity
            if currDays <= days:
                leastWeight = min(mid, leastWeight)
                heigh = mid - 1
            else:
                low = mid + 1
        
        return leastWeight

