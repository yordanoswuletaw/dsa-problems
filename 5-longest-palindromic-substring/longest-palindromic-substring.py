class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        def find_palindrom(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right

        start = end = 0
        for i in range(n):
            left, right = find_palindrom(i, i)
            if end - start < right - left:
                start, end = left, right
            
            left, right = find_palindrom(i, i + 1)
            if end - start < right - left:
                start, end = left, right
        
        return s[start:end]