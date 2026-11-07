"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        isort = sorted(intervals, key = lambda x: x.start)

        for i in isort:
            print([i.start, i.end])

        heap = []
        count = 0

        for i in isort:

            if not heap or heap[0] > i.start:
                count += 1

            else:
                heapq.heappop(heap)

            heapq.heappush(heap, i.end)

        return count

        