class Solution:
    def countSubstrings(self, s: str) -> int:

        self.count_palindrome = 0

        n = len(s)
        def helper():

            ## for odd:
            for i in range(n):
                
                left = i
                right = i

                while (left >= 0) and (right < n) and s[left] == s[right]:
                    self.count_palindrome += 1
                    
                    left -= 1
                    right += 1
            
            ## for even:
            for i in range(n-1):
                if s[i] == s[i+1]:
                    left = i
                    right = i + 1

                    while (left >= 0) and (right < n) and s[left] == s[right]:
                        self.count_palindrome += 1
                        
                        left -= 1
                        right += 1

        

        
        helper()
        return self.count_palindrome




        
        