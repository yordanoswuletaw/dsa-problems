class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n, m = len(s), len(wordDict)
        wordSet = set(wordDict)
        memo = defaultdict(bool)

        def dp(start_indx):
            if start_indx == n:
                return True
            
            if start_indx in memo:
                return memo[start_indx]
            
            
            for end_indx in range(start_indx, n):
                if s[start_indx:end_indx + 1] in wordSet:
                    memo[start_indx] |= dp(end_indx + 1)
                    if memo[start_indx]:
                        return True
            
            return False
        
        return dp(0)
        