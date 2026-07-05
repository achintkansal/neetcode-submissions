"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda x: x.start)

        prev_start, prev_end = intervals[0].start, intervals[0].end
        for pair in intervals[1:]:
            curr_start, curr_end = pair.start, pair.end

            if curr_start < prev_end:
                return False
            
            prev_start, prev_end = curr_start, curr_end
        
        return True


