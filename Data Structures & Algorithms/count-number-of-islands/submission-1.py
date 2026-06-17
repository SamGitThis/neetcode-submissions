class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rw, cl = len(grid), len(grid[-1])
        count = 0

        def bfs(r, c):
            if r >= rw or r < 0 or c >= cl or c < 0 or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            bfs(r, c+1)
            bfs(r, c-1)
            bfs(r-1, c)
            bfs(r+1, c)

        for r in range(rw):
            for c in range(cl):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r, c)

        return count