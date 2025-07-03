class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = []
        for occ, char in (a, 'a'), (b, 'b'), (c, 'c'):
            if occ > 0:
                heapq.heappush(heap, (-occ, char))
                
        longest_string = []
        while heap:
            occ, char = heapq.heappop(heap)
            needed = min(abs(occ), 2)
            occ += needed
            if longest_string and longest_string[-1] == char:
                if not heap:
                    break
                _occ, _char = heapq.heappop(heap)
                _occ += 1 
                longest_string.append(_char)
                if _occ < 0:
                    heapq.heappush(heap, (_occ, _char))
            longest_string.extend([char] * needed)
            if occ < 0:
                heapq.heappush(heap, (occ, char))
        
        return ''.join(longest_string)
        