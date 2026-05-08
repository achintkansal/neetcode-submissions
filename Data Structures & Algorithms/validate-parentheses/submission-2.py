from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        n = len(s)
        i = 0

        close_open = {']': '[', '}': '{', ')': '('}
        
        while i < n:
            print(stack)
            if s[i] in close_open:
                if len(stack) > 0 and close_open[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            i += 1

        if len(stack) > 0:
            return False
        return True 
        