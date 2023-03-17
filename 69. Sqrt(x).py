class Solution:
    def mySqrt(self, x: int) -> int:

        low, heigh = 0, x // 2 + 1
        while low <= heigh:
            mid = low + (heigh - low + 1) // 2
            if mid * mid == x:
                return mid 
            elif mid * mid > x:
                heigh = mid - 1
            else:
                low = mid + 1
        return heigh
