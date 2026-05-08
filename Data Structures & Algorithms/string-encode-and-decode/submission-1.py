class Solution:

    def encode(self, strs: List[str]) -> str:
        str_ans = ''
        for str1 in strs:
            str_ans += f'{len((str)(len(str1)))}'+f'{len(str1)}' + str1
        print(str_ans)
        return str_ans
    def decode(self, s: str) -> List[str]:
        str_ans = []
        i = 0
        while(i < len(s)):
            n1 = (int)(s[i])
            n = (int)(s[i+1:i+1+n1])    
            str_ans.append(s[i+n1+1:i+n1+n+1])
            i = i+n1+n+1    
        return str_ans
