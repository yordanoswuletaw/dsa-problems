class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        state = None
        ans = []
        for i in range(len(groups)):
            if groups[i] != state:
                ans.append(words[i])
                state = groups[i]
        
        return ans
        