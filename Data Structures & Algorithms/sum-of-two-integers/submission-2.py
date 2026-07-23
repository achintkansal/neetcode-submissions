class Solution:
    def getSum(self, a: int, b: int) -> int:

        s1 = 0
        s2 = 0
        carry = 0

        res = 0
        print(f"{a:b}")
        print(f"{b:b}")
        
        for i in range(32):

            s1 = a & 1
            s2 = b & 1

            if (s1 == 1) and (s2 == 1):
                if carry == 1:
                    res |= 1 << i
                carry = 1
                
            elif (s1 != s2):
                if (carry == 0):
                    res |= 1 << i
                else:
                    carry = 1
            
            else:
                if carry == 1:
                    res |= 1 << i
                    carry = 0
            
            a = a >> 1
            b = b >> 1

        if res > (2**31 - 1):
            res = ~(res ^ ((2 ** 32) - 1))
        print(f'{res:b}')
        return res
            
            
        