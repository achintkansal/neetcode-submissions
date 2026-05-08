class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        window = {} # character : index
        left = 0
        right = 0
        max_len = 0
        while right < n:
            if (s[right] in window) and (window[s[right]] >= left):
                left = window[s[right]] + 1

            window[s[right]] = right
            max_len = max(max_len, right - left + 1)
            right += 1
            
        print(window)
        return max_len


        