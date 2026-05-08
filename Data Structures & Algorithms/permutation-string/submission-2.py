class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq1 = [0] * 26
        freq2 = [0] * 26
        m = len(s1)
        n = len(s2)

        if m > n:
            return False
        left = 0
        right = m

        for i in range(m):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        
        if tuple(freq1) == tuple(freq2):
            return True

        while right < n:

            freq2[ord(s2[right]) - ord('a')] += 1
            freq2[ord(s2[left]) - ord('a')] -= 1

            if tuple(freq1) == tuple(freq2):
                return True
            left += 1
            right += 1

            
        
        return False
            
        