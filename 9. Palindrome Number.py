class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        val, res = x, 0
        while val:
            res = res * 10 + val % 10
            val //= 10
        return x == res
