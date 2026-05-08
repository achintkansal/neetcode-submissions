class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        right = 0

        max_len = 0
        
        def index(ch):
            return (ord(ch) - ord('A'))

        freq = [0] * 26
        max_freq = 0
        while right < n:
            freq[index(s[right])] += 1
            max_freq = max(freq[index(s[right])], max_freq)
            sub_len = right - left + 1
            k_out = sub_len - max_freq

            while k_out > k:
                freq[index(s[left])] -= 1
                left += 1
                sub_len = right - left + 1
                k_out = sub_len - max_freq
            
            max_len = max(max_len, sub_len)
            right += 1
        
        return max_len





        