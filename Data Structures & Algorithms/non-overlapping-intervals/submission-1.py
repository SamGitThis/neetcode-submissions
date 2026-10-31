class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        isort = sorted(intervals, key = lambda i: i[1])
        prev = float('-inf')
        count = 0

        for start, end in isort:
            if prev <= start:
                prev = end
            else:
                count += 1

        return count
            