class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def freq_element(freq):
            max_freq = 0
            for f in freq:
                max_freq = max(max_freq, f)
            return max_freq
        
        freq = [0] * 26

        ## len(window) - high_freq <= k

        l = 0
        r = 0
        res = 0
        while r < len(s):
            freq[ord(s[r]) - ord('A')] += 1
            window = r - l + 1
            max_freq = freq_element(freq)
            if window - max_freq <= k:
                res = max(res, window)
            else:

                while (l < r) and ((window - max_freq) > k):
                    freq[ord(s[l]) - ord('A')] -= 1
                    l += 1
                    window = r - l + 1
                    max_freq = freq_element(freq)
            r += 1
        
        return res
                    



        