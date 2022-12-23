class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        # using ASCII value of alphanumeric characters
        while i < j:
            start, end = s[i].lower(), s[j].lower()
            if (ord(start) < 48 or ord(start) > 57) and (ord(start) < 97 or ord(start) > 122):
                i += 1
            elif (ord(end) < 48 or ord(end) > 57) and (ord(end) < 97 or ord(end) > 122):
                j -= 1
            else:
                if start != end:
                    return False
                i += 1
                j -= 1
        return True 
        
