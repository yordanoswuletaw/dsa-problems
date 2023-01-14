class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        real1, imag1 = self.extract(num1)
        real2, imag2 = self.extract(num2)

        return str(real1 * real2 - imag1 * imag2) + '+' + str(real1 * imag2 + imag1 * real2) + 'i'

    def extract(self, nums):
        real, imag = nums.split('+')
        return int(real), int(imag[:-1])
        
