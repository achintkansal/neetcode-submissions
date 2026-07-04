class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        map_dig = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
        }

        res = []
        subset = []
        if len(digits) == 0:
            return res
        n = len(digits)
        def helper(i):
            if i == n:
                res.append("".join(subset))
                return
            pos_ch = map_dig[digits[i]]
            for j in range(len(pos_ch)):
                subset.append(pos_ch[j])
                helper(i+1)
                subset.pop()
        
        helper(0)
        return res
        