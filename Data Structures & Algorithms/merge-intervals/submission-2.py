class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        isort = sorted(intervals, key = lambda i: i[0])
        ans = []

        print(isort)

        for start, end in isort:
            if not ans or ans[-1][1] < start:
                ans.append([start, end])

            else: ans[-1][1] = max(ans[-1][1], end)

        return ans