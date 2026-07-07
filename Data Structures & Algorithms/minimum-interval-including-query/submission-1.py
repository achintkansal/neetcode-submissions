class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        res = []
        for q in queries:
            curr_res = float('inf')
            for interval in intervals:
                start, end = interval[0], interval[1]
                if start <= q and end >= q:
                    curr_res = min(curr_res, end-start+1)
            
            if curr_res == float('inf'):
                curr_res = -1
            
            res.append(curr_res)
        
        return res



        