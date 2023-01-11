class Solution:
    def printVertically(self, s: str) -> List[str]:

        s = list(s.split())
        maxWordLen = len(max(s, key = lambda char: len(char)))
        for i in range(len(s)):
            s[i] = s[i] + ' ' * (maxWordLen - len(s[i]))
        output = ['' for i in range(maxWordLen)]

        for i, word in enumerate(s):
            for j in range(len(word)):
                output[j] += word[j]        
        
        return [each.rstrip() for each in output]
