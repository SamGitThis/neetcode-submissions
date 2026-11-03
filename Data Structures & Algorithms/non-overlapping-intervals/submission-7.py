class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        isort = sorted(intervals, key = lambda i: i[0])
        ans = []
        
        for start, end in isort:
            if not ans or ans[-1][1] <= start:
                ans.append([start, end])
            else:
                if end > ans[-1][1]:
                    pass
                else:
                    ans.pop()
                    ans.append([start, end])
        print(isort)
        print(ans)
        return len(intervals) - len(ans)