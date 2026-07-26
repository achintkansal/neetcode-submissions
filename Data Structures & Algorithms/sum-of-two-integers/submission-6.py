class Solution:
    def getSum(self, a: int, b: int) -> int:

        ## Method2: Video: But small and good
        ## for sum take xor and for migrating carry do 'and' operation

        res = a ^ b
        carry = a & b
        bits = 0
        while (carry != 0) and bits <32:
            carry = carry << 1 #for carry to populate until all the carries are populated
            
            res_new = res ^ carry
            carry = res & carry

            res = res_new
            bits += 1
        
        return res


        ## Method 1: Self
        # s1 = 0
        # s2 = 0
        # carry = 0

        # res = 0
        # print(f"{a:b}")
        # print(f"{b:b}")
        
        # for i in range(32):

        #     s1 = a & 1
        #     s2 = b & 1

        #     if (s1 == 1) and (s2 == 1):
        #         if carry == 1:
        #             res |= 1 << i
        #         carry = 1
                
        #     elif (s1 != s2):
        #         if (carry == 0):
        #             res |= 1 << i
        #         else:
        #             carry = 1
            
        #     else:
        #         if carry == 1:
        #             res |= 1 << i
        #             carry = 0
            
        #     a = a >> 1
        #     b = b >> 1

        # if res > (2**31 - 1):
        #     res = ~(res ^ ((2 ** 32) - 1))
        # # print(f'{res:b}')
        # return res

## For 2's complement refer to the notes here
## In this problem... We assumed the integer is 32 bit integer... But in python
## it is not 32bits... hence last condition if res > (2**31 - 1): res = ~(res ^ ((2 ** 32) - 1)) = making all leftmost bits 111s

            
            
        