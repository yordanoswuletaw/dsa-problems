class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        hashMap = Counter(sorted(words))
        heap = [(-value, key) for key, value in hashMap.items()]
        heapify(heap)
        output = []
        for _ in range(k):
            output.append(heappop(heap)[1])      
        
        return output
