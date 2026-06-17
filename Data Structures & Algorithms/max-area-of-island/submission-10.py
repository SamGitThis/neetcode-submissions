class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mland = 0
        fin = 0
        rw, cl = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal mland
            if r >= rw or r < 0 or c >= cl or c < 0 or grid[r][c] == 0:
                return 

            mland += 1
            grid[r][c] = 0
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        for r in range(rw):
            for c in range(cl):
                if grid[r][c] == 1:
                    dfs(r, c)
                    fin = max(fin, mland)
                    mland = 0

        return fin