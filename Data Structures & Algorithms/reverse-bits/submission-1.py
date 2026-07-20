class Solution:
    def reverseBits(self, n: int) -> int:


        res = 0
        # ## 1st way
        # for i in range(32):
        #     bit = (n >> i) & 1
        #     if bit:
        #         res = res | 1 << (31-i)
        
        # return res
        i = 0
        while n > 0:
            bit = n & 1
            res |= 1 << (31-i) if bit else 0
            n = n >> 1
            i += 1
        return res


        