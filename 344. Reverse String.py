class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # using iteration
        # leftPtr, rightPtr = 0, len(s) - 1
        # while leftPtr < rightPtr:
        #     s[leftPtr], s[rightPtr] = s[rightPtr], s[leftPtr]
        #     leftPtr += 1
        #     rightPtr -= 1

        # using recursion
        self.reverse(s, 0, len(s) - 1)

    def reverse(self, s, left, right):
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        self.reverse(s, left + 1, right - 1)
    
        
