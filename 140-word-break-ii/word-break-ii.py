class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        n, m = len(s), len(wordDict)
        wordSet = set(wordDict)
        memo = defaultdict(list)

        ans = []
        def dp(start_indx, sentence):
            if start_indx == n:
                ans.append(' '.join(sentence))
                return
            
            for end_indx in range(start_indx, n):
                if s[start_indx:end_indx + 1] in wordSet:
                    dp(end_indx + 1, sentence +  [s[start_indx:end_indx + 1]])
        
        dp(0, [])
        return ans


            
        