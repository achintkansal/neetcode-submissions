class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        new_start = newInterval[0]
        new_end = newInterval[1]

        res = []
        i = 0
        for pair in intervals:
            start, end = pair[0], pair[1]

            if new_start > end:
                res.append(pair)      
            else:
                break   
            i += 1
        
        if i == n:
            res.append(newInterval)
            return res
        
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]

            if new_end < start:
                res.append([new_start, new_end])
                break

            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
            
            i += 1
        
        if i < n:
            res.extend(intervals[i:])
        else:
            res.append([new_start, new_end])

        return res



        

        