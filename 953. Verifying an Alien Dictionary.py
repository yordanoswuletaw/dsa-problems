class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        orderMap = {}
        for i,ord in enumerate(order):
            orderMap[ord] = i
        for i in range(1, len(words)):
            prev, curr = words[i-1], words[i]
            for i in range(len(prev)):
                if i >= len(curr):
                    return False
                elif orderMap[prev[i]] > orderMap[curr[i]]:
                    return False
                elif orderMap[prev[i]] < orderMap[curr[i]]:
                    break
        return True 
