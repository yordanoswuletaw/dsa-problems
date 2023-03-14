class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # with out loop/recursion
        if n <= 0:
            return False
        res = log(n, 4)
        return res == int(res)

        # using recursion
        if n < 1:
            return False
        elif n == 1:
            return True 
        return self.isPowerOfFour(n / 4)
