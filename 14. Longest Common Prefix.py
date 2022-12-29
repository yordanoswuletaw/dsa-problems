class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ''
        mid = len(strs) // 2
        left = self.longestCommonPrefix(strs[:mid])
        right = self.longestCommonPrefix(strs[mid:])
        return self.resolvePrefix(left, right)
    
    def resolvePrefix(self,left, right):
        prfx = left if len(left) < len(right) else right
        for i in range(min(len(left), len(right))):
            if left[i] != right[i]:
                return left[:i]
        return prfx
             
