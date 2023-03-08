class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        prfxSum = [0] * (n + 1)
        ltrs = list(s)
        # range sum
        for shift in shifts:
            if shift[2]:
                prfxSum[shift[0]] += 1
                prfxSum[shift[1] + 1] -= 1
            else:
                prfxSum[shift[0]] -= 1
                prfxSum[shift[1] + 1] += 1
        
        for i in range(1, len(prfxSum)):
            prfxSum[i] += prfxSum[i-1]
        
        print(prfxSum)
        
        for i in range(n):
            # shifting characters
            val = ord(ltrs[i]) + (prfxSum[i] % 26)
            ltrs[i] = chr(97 + (val - 97) % 26)
        
        return ''.join(ltrs)
        
