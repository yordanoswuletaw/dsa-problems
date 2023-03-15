class Solution:
    def countGoodNumbers(self, n: int) -> int:

        modulo = 10 ** 9 + 7
        res = pow( 5 * 4, n // 2, modulo)
        return 5 * res % modulo if n % 2 else res
       
