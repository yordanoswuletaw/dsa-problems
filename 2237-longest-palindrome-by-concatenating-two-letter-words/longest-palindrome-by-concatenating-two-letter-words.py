class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        longest_pal = odd = 0
        hash_map = Counter(words)
        for word, val in hash_map.items():
            if word[0] == word[1]:
                if hash_map[word] % 2:
                    odd = 2
                    val -= 1
                longest_pal += 2 * val
            elif word[::-1] in hash_map:
                val = min(val, hash_map[word[::-1]])
                hash_map[word[::-1]] = 0
                longest_pal += 4 * val
            hash_map[word] = 0
        
        return longest_pal + odd