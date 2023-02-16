class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        l, r = 0, int(c ** 0.5)
        while l <= r:
            eq = (l ** 2) + (r ** 2)
            if eq == c:
                return True 
            elif eq > c:
                r -= 1
            else:
                l += 1
        
        return False
