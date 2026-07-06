"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start, end = [], []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        s, e = 0, 0
        n = len(intervals)
        meeting = 0
        res = 0
        while s < n:
            if start[s] < end[e]:
                s += 1
                meeting += 1
            else:
                e += 1
                meeting -= 1
            
            res = max(meeting, res)
        return res
            


        