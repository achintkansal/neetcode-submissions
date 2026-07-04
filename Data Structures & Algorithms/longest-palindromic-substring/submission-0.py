class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.max_reslen = 1
        max_res = [s[0]]

        n = len(s)
        def helper():

            ## for odd:
            for i in range(n):
                if (i > 0) and (i < n-1):
                    left = i-1
                    right = i+1

                    while (left >= 0) and (right < n) and s[left] == s[right]:
                        if self.max_reslen < (right - left + 1): 
                            self.max_reslen = right - left + 1
                            max_res[0] = s[left:right+1]
                        
                        left -= 1
                        right += 1
            
            ## for even:
            for i in range(n-1):
                if s[i] == s[i+1]:
                    left = i
                    right = i + 1

                    while (left >= 0) and (right < n) and s[left] == s[right]:
                        if self.max_reslen < (right - left + 1): 
                            self.max_reslen = right - left + 1
                            max_res[0] = s[left:right+1]
                        
                        left -= 1
                        right += 1

        

        
        helper()
        return max_res[0]




        
        