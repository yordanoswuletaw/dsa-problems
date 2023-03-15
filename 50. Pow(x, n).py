class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 0
        
        res = self.computePow(x, abs(n))
        return res if n > 0 else 1/res

    def computePow(self, x, n):
        if n == 0:
            return 1
        res = self.computePow(x, n // 2) 
        res = res * res 
        return res * x if n % 2 else res
       
        
