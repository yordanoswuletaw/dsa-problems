class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        #initial depth
        stack = [0]

        for each in s:
            if each == '(':
                stack.append(0)
            else:
                currDepth = stack.pop()
                stack[-1] += max(currDepth * 2, 1)
        
        return stack.pop()


        # stack = []

        # for each in s:
        #     if each == ')':
        #         if stack[-1] == '(':
        #             stack.pop()
        #             stack.append(1)
        #         else:
        #             while True:
        #                 outer = stack.pop()
        #                 inner = stack.pop()
        #                 if inner == '(':
        #                     stack.append(2 * outer)
        #                     break
        #                 else:
        #                     stack.append(outer + inner)
        #     else:
        #         stack.append(each)
        
        # return sum(stack)
