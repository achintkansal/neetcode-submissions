class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def generate_helper(open, close, curr_ans):

            if (open == 0) and (close == 0):
                ans.append(curr_ans)
                return

            if close < open:
                return
            if open == 0:
                curr_ans = curr_ans + ')'
                generate_helper(open, close - 1, curr_ans)
                curr_ans = curr_ans[:-1]
                return
            
            
            curr_ans = curr_ans + '('
            generate_helper(open-1, close, curr_ans)
            curr_ans = curr_ans[:-1]

            curr_ans = curr_ans + ')'
            generate_helper(open, close-1, curr_ans)
            curr_ans = curr_ans[:-1]

        generate_helper(n , n, "")

        return ans
            





        