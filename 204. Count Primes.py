class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 1:
            return 0

        primes = [True] * n 
        primes[0] = primes[1] = False

        indx = 2
        while indx * indx <= n:
            if primes[indx]:
               num = indx * indx
               while num < n:
                   primes[num] = False
                   num += indx
            indx += 1
        
        return primes.count(True)


        
