class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low, heigh = 1, sum(weights)
        leastWeight = heigh

        if days == 1:
            return heigh
        elif days == len(weights):
            return max(weights)

        while low <= heigh:
            mid = low + (heigh - low) // 2
            maxWeight = currDay = weightSum = 0
            for weight in weights:
                if weightSum + weight > mid:
                   currDay += 1
                   maxWeight = max(maxWeight, weightSum)
                   weightSum = 0
                weightSum += weight
            if weightSum :
                currDay += 1
            
            if currDay <= days:
                leastWeight = min(maxWeight, leastWeight) 
                heigh = mid - 1
            else:
                low = mid + 1
        
        return leastWeight
