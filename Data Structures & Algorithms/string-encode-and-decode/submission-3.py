class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            n = len(s)
            encoded = encoded+str(n)+"#"+s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        res = []
        while i < n:
            len_str = ""
            while s[i] >= '0' and s[i] <= '9':
                len_str = len_str + s[i]
                i += 1
            print(len_str)
            if s[i] == '#':
                i += 1
            l = int(len_str)
            orig = "".join(s[i:i+l])
            res.append(orig)
            i = i+l
        return res



