class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            print(stack)
            if tokens[i] in operators:
                val1 = stack.pop()
                val2 = stack.pop()

                if tokens[i] == '+':
                    stack.append(val2 + val1)
                elif tokens[i] == '-':
                    stack.append(val2 - val1)
                elif tokens[i] == '*':
                    stack.append(val2 * val1)
                elif tokens[i] == '/':
                    stack.append(int(val2 / val1))
            
            else:
                stack.append(int(tokens[i]))
                
        
        return stack.pop()