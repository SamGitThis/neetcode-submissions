"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        inter = []
        for interval in intervals:
            inter.append([interval.start, interval.end])
        inter = sorted(inter, key = lambda i: i[0])

        prev = float('-inf')
        print(inter)

        for start, end in inter:
            if prev > start:
                return False
            else:
                prev = end

        return True