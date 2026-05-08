from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        n = len(s)
        i = 0

        open = ['[', '{', '(']
        close = [']', '}', ')']
        while i < n:
            if s[i] in open:
                stack.append(s[i])
            
            else:
                if len(stack) > 0:
                    index = open.index(stack[-1])
                    print(index)
                    expected_close = close[index]
                    if s[i] == expected_close:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            
            i += 1
        
        if len(stack) > 0:
            return False
        return True 
        