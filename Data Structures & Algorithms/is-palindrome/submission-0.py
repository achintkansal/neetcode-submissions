class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def preprocess(s):
            s = s.lower()
            new_str = ""
            for ch in s:
                if (ch >= 'a' and ch <= 'z'):
                    new_str = new_str + ch
                
                if (ch >= '0' and ch <= '9'):
                    new_str = new_str + ch
                
            return new_str
        s = preprocess(s) 
        j = len(s) - 1
        i = 0
        print(s)  
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
        