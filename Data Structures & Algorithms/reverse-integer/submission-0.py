class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        low_range = -1 * 2**31
        high_range = 2**31 - 1
        if x < 0:
            sign = -1
            x = x * -1

        rev = 0
        while x > 0:
            d = x % 10
            rev = rev*10 + d
            x = x // 10
        
        rev *= sign
        if (rev < low_range) or (rev > high_range):
            return 0
        
        return rev

        