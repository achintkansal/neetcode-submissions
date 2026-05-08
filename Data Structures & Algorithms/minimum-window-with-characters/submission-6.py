class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_s = [0] * 256
        freq_t = [0] * 256

        if len(s) < len(t):
            return ""

        def check_substring(freq1, freq2): ## freq1 substring
            for i in range(256):
                if freq1[i] > freq2[i]:
                    return False
            return True
        
        
        for ch in t:
            freq_t[ord(ch)] += 1
        
        l, r = 0, 0
        n = len(s)
        
        min_str = ""
        min_len = float('inf')
        # print(freq_t)
        # print(freq_s)
        while r < n:
            freq_s[ord(s[r])] += 1
            r += 1
            
            while check_substring(freq_t, freq_s) and (l < r):
                
                if min_len > (r-l):
                    min_len = r-l
                    min_str = s[l:r]
                
                freq_s[ord(s[l])] -= 1
                l = l+1
            
            
        return min_str





        

        