class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        result = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            # comparing the next words 
            if word1[i:] > word2[j:]:
                result.append(word1[i])
                i += 1
            else:
                result.append(word2[j])
                j += 1
        # concatinating remaining words
        result.extend(word1[i:])
        result.extend(word2[j:])
        return ''.join(result)
