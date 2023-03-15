class Solution:
 
    def decodeString(self, s: str) -> str:

        stack, n = [], len(s)

        for i in range(n):
            if s[i] == ']':
                strs, digits = deque(), deque()
                # extracting strings from stack
                while stack and stack[-1] != '[':
                    strs.appendleft(stack.pop())
                # poping '[' out of stack
                stack.pop()
                # extracting digits from stack
                while stack and stack[-1].isdigit():
                    digits.appendleft(stack.pop())
                
                stack.append(int(''.join(digits)) * ''.join(strs))

            else:
                stack.append(s[i])
        
        return ''.join(stack)
