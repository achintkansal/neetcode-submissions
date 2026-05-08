class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        for ch in s1:
            freq_s1[ord(ch) - ord('a')] += 1
        
        l = 0
        r = 0
        while r < n:
            freq_s2[ord(s2[r]) - ord('a')] += 1
            r += 1
        
        while r < m:
            if tuple(freq_s1) == tuple(freq_s2):
                return True
            
            freq_s2[ord(s2[r]) - ord('a')] += 1
            freq_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
        if tuple(freq_s1) == tuple(freq_s2):
            return True

        return False

        