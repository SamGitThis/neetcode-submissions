class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = 0
        fi = 0

        def area(r, c):
            nonlocal m
            rl, cl = len(grid), len(grid[0])
            if (r >= rl or r < 0 or c >= cl or c < 0 or grid[r][c] == 0):
                return
            
            m += 1
            grid[r][c] = 0
            area(r, c+1)
            area(r, c-1)
            area(r+1, c)
            area(r-1, c)
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area(r, c)
                    fi = max(fi, m)
                    m = 0

        return fi
