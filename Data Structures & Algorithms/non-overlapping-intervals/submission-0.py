class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []

        intervals.sort(key = lambda i: i[0])

        prev_start, prev_end = intervals[0][0], intervals[0][1]

        for pair in intervals[1:]:

            curr_start, curr_end = pair[0], pair[1]

            if prev_end <= curr_start:
                res.append([prev_start, prev_end])
                prev_start, prev_end = curr_start, curr_end
            else:
                if curr_end < prev_end:
                    prev_start, prev_end = curr_start, curr_end
        
        res.append([prev_start, prev_end])
        n = len(intervals)
        return n - len(res)

        