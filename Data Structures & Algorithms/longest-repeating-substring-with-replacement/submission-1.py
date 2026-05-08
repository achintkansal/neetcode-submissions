class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        right = 0

        max_len = 0
        
        def index(ch):
            return (ord(ch) - ord('A'))

        freq = [0] * 26
        while right < n:
            freq[index(s[right])] += 1
            sub_len = right - left + 1
            k_out = sub_len - max(freq)

            while k_out > k:
                freq[index(s[left])] -= 1
                left += 1
                sub_len = right - left + 1
                k_out = sub_len - max(freq)
            
            max_len = max(max_len, sub_len)
            right += 1
        
        return max_len





        