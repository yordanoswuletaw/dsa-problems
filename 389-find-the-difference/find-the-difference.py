class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = sum(ord(char) for char in s)
        t_sum = sum(ord(char) for char in t)
        
        return chr(t_sum - s_sum)
        