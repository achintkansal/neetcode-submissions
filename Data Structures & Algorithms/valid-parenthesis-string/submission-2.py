class Solution:
    def checkValidString(self, s: str) -> bool:

        open_min = 0
        open_max = 0 ## we will maintain a range from [open_min, open_range]; if 0 lies within this range, then we return true

        for i in range(len(s)):

            if s[i] == '(':
                open_min += 1
                open_max += 1
            
            elif s[i] == ')':
                open_min -= 1
                open_max -= 1
            
            else: ## '*'
                open_min -= 1
                open_max += 1
        
        return True if (open_min <= 0) and (0 <= open_max) else False

            


        