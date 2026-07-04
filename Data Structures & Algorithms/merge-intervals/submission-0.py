class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        interval_s = sorted(intervals, key = lambda x: x[0])

        res = []
        n = len(interval_s)
        prev_start, prev_end = interval_s[0][0], interval_s[0][1]
        for i in range(1,n):
            
            curr_start, curr_end = interval_s[i][0], interval_s[i][1]
            if curr_start > prev_end: ## if non overlapping previous element put it into result
                res.append([prev_start, prev_end])
                prev_start = curr_start
                prev_end = curr_end
            else:
                prev_start = min(prev_start, curr_start)
                prev_end = max(prev_end, curr_end)
            
        
        res.append([prev_start, prev_end])
        return res

        