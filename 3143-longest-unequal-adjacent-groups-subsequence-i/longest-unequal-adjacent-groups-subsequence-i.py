class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        state = groups[0]
        ans = [words[0]]
        for i in range(1, len(groups)):
            if groups[i] != state:
                ans.append(words[i])
                state = groups[i]
        
        return ans
        