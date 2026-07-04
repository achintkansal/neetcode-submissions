class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        new_start = newInterval[0]
        new_end = newInterval[1]

        res = []
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if new_start > end: ## to skip the intervals who are smaller
                res.append(intervals[i])      
            elif start > new_end: ## to insert an interval and then return
                res.append([new_start, new_end])
                res.extend(intervals[i:])
                return res
            else: ## for overlapping change new_start and new_end
                new_start = min(intervals[i][0], new_start)
                new_end = max(intervals[i][1], new_end)

        res.append([new_start, new_end])
        return res 