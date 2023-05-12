class Solution:
    def findComplement(self, num: int) -> int:
       n = num.bit_length()
       compNum =  2 ** n - 1
       return num ^ compNum
