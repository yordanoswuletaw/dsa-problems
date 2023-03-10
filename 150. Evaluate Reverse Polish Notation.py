class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
    
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                rightOp, leftOp = stack.pop(), stack.pop()
                
                if token == '+':
                    stack.append(int(leftOp) + int(rightOp))
                elif token == '-':
                    stack.append(int(leftOp) - int(rightOp))
                elif token == '*':
                    stack.append(int(leftOp) * int(rightOp))
                else:
                    stack.append(int(int(leftOp) / int(rightOp)))
               
            else:
                stack.append(token)
        
        return int(stack.pop())
