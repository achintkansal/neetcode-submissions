class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_list1 = [0] * 26
        freq_list2 = [0] * 26
        
        n = len(s)
        m = len(t)

        if n != m:
            return False
        
        for i in range(n):
            freq_list1[ord(s[i]) - ord('a')] += 1
            freq_list2[ord(t[i]) - ord('a')] += 1
        
        for i in range(26):
            if freq_list1[i] != freq_list2[i]:
                return False
        return True
        