class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        s = sorted(intervals, key = lambda x: x[1])
        count = 0
        prev_end = float('-inf')

        print(s)
        for start, end in s:
            if prev_end <= start:
                prev_end = end
                continue
            else:
                count += 1

        return count