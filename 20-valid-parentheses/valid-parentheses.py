class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif not stack:
                return False
            elif char == ')' and stack[-1] != '(':
                return False
            elif char == '}' and stack[-1] != '{':
                return False
            elif char == ']' and stack[-1] != '[':
                return False
            else:
                stack.pop()
        
        return not stack
        