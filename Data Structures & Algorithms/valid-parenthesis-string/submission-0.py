class Solution:
    def checkValidString(self, s: str) -> bool:

        ## backtracking
        # stack = []
        n = len(s)

        def check(i, stack):
            
            if (i == n) and len(stack) == 0:
                return True
            
            if (i == n) and len(stack) > 0:
                return False

            if s[i] == '(':
                stack.append('(')
                return check(i+1, stack.copy())

            elif s[i] == ')':
                if (len(stack) > 0) and (stack[-1] == '('):
                    stack.pop()
                    return check(i+1, stack.copy())
                else:
                    return False
            else:
                stack.append('(')
                ans1 = check(i+1, stack.copy())
                stack.pop()

                ## for ')' bracket
                if (len(stack) > 0) and (stack[-1] == '('):
                    stack.pop()
                    ans2 = check(i+1, stack.copy())
                    stack.append('(')
                else:
                    ans2 = False

                ans3 = check(i+1, stack.copy())

                return (ans1 or ans2 or ans3)
        
        
        return check(0, [])

        