"""
u: find the min meeting rooms necessary to hold all meetings
meeting times will always be valid 
meeting times can be inclusive but not overlap
input: 2d array of meeting intervals
output: min number of meeting rooms
edge cases:
- empty array  
    - return 0
- all overlap
    - return size of array
- consecutive meetings
    - return 1
"""


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
        start.sort()

        end = []
        for i in range(len(intervals)):
            end.append(intervals[i].end)
        end.sort()

        s = 0
        e = 0
        res = 0
        count = 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res