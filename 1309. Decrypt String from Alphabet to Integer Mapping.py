class Solution:
    def freqAlphabets(self, s: str) -> str:
        decryptedString = ''
        i = len(s) - 1
        # to easly access characters between 'j' to 'z' i started at the end of the string 's'
        while i >= 0:
            # if the current character is '#' then i will move i two steps and decode the character
            if s[i] == '#':
                 decryptedString = chr(96 + int(s[i-2] + s[i - 1])) + decryptedString
                 i -= 3
            else:
                decryptedString = chr(96 + int(s[i])) + decryptedString
                i -= 1
        return decryptedString
