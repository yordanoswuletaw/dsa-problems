class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []
        heapify(heap)

        for stone in stones:
            heappush(heap, -1 * stone)
        
        while len(heap) > 1:
            stone1 = abs(heappop(heap))
            stone2 = abs(heappop(heap))
            remWeight = abs(stone1 - stone2)
            if remWeight:
                heappush(heap, -1 * remWeight)

        return abs(heappop(heap)) if len(heap) else 0
        
