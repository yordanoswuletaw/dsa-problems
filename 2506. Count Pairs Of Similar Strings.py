class Solution:
    def similarPairs(self, words: List[str]) -> int:

        hashMap = {}
        pairs = 0
        for word in words:
           x = ''.join(sorted(set(word)))
           pairs += hashMap.get(x, 0)
           hashMap[x] = hashMap.get(x, 0) + 1
        return pairs

        
