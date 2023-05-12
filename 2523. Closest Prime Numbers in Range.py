class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        primes = [True] * (right + 1)
        primes[0] = primes[1] = False

        # generate all primes up to right
        def generate():

            prime = 2
            while prime * prime <= right:
                if primes[prime]:
                    notPrime = prime * prime
                    while notPrime <= right:
                        primes[notPrime] = False
                        notPrime += prime
                prime += 1
        
        generate()

        # finding pairs of primes that has minimum difference
        start, end = 0,  left
        ans = []

        while end < len(primes):
            if primes[end]:
                if not primes[start]:
                    start = end
                else:
                    if not ans:
                        ans.append(start)
                        ans.append(end)
                    elif ans[1] - ans[0] > end - start:
                        ans[0] = start
                        ans[1] = end
                    start = end
            end += 1

        return ans if ans else [-1, -1]


