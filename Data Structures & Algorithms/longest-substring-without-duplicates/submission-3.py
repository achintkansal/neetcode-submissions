class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0

        def index(ch):
            return (ord(ch))

        index_arr = [-1] * 256
        longest = 0
        while right < n:

            if index_arr[index(s[right])] >= 0: 
                l = index_arr[index(s[right])] + 1
                if l > left:
                    left = l
            
            index_arr[index(s[right])] = right
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest


        