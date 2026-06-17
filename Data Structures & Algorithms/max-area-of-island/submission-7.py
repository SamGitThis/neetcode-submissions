class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mas = [0]
        ma = 0

        def dfs(r, c):
            nonlocal ma
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return
            grid[r][c] = 0
            ma += 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    mas.append(ma)
                    ma = 0
        
        return max(mas)