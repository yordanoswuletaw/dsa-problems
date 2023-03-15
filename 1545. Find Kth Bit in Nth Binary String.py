class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def helper(indx):
            if indx == 1:
                return '0'
            prev = helper(indx - 1)
            # appending '1'
            res = prev + "1"
            # appending reverse(invert(Si-1))
            for each in prev[::-1]:
                res += "1" if each == '0' else '0'
            return res
        

        return helper(n)[k - 1]

