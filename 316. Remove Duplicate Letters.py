class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        freq = {num: i for i, num in enumerate(s)}
        stack, seen = [], set()

        for i, char in enumerate(s):
            # pop if top of stack exist in the future and is greater than current char
            while stack and stack[-1] > char and char not in seen and i < freq[stack[-1]]:
                seen.remove(stack[-1])
                stack.pop()
            
            if char not in seen:
                stack.append(char)
                seen.add(char)
        
        return ''.join(stack)
