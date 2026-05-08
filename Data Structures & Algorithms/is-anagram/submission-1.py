class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        if len(s) != len(t):
            return False
        
        n = len(s)
        for i in range(n):
            freq1[ord(s[i]) - ord('a')] += 1
            freq2[ord(t[i]) - ord('a')] += 1
        
        return tuple(freq1) == tuple(freq2)
            

        