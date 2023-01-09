class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        res = ''
        j = 0
        for i in range(len(s)):
            if j < len(spaces): 
                if i == spaces[j]:
                     res += ' ' + s[i]
                     j += 1
                else:
                    res += s[i]
            else:
                res += s[i:]
                break
        return res
