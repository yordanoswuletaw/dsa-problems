class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        prfxSum = [0] * 1001

        for trip in trips:
            prfxSum[trip[1]] += trip[0]
            prfxSum[trip[2]] -= trip[0]

        for i in range(1, 1001):
            prfxSum[i] += prfxSum[i - 1]
        
        for each in prfxSum:
            if each > capacity:
                return False 
        
        return True
