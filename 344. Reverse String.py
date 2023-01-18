class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftPtr, rightPtr = 0, len(s) - 1
        while leftPtr < rightPtr:
            s[leftPtr], s[rightPtr] = s[rightPtr], s[leftPtr]
            leftPtr += 1
            rightPtr -= 1
        
